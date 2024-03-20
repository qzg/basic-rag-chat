import hmac
import pandas as pd
import streamlit as st
from pathlib import Path
import uuid
import os

from langchain.schema import AIMessage, HumanMessage
from langchain.schema.runnable import RunnableMap
from langchain.callbacks.base import BaseCallbackHandler
from models import load_embedding_model, load_llm
from prompts import load_prompt
from database import load_vectorstore, load_memory, load_chat_history, load_retriever, vectorize_text

# Streaming call back handler for responses
class StreamHandler(BaseCallbackHandler):
    def __init__(self, container, initial_text=""):
        self.container = container
        self.text = initial_text

    def on_llm_new_token(self, token: str, **kwargs):
        self.text += token
        self.container.markdown(self.text + "▌")


def init_ui():
    print("init_ui")
    print(st.session_state)
    # Get a unique session id for memory
    if "session_id" not in st.session_state:
        st.session_state.session_id = uuid.uuid4()

    # Start with empty messages, stored in session state
    if 'messages' not in st.session_state:
        st.session_state.messages = [AIMessage(content=st.session_state.lang_dict.get('assistant_welcome', 'Welcome to the AI Assistant'))]


# Close off the app using a password
def check_password():
    print("check_password")
    print(st.session_state)
    """Returns `True` if the user had a correct password."""

    def login_form():
        """Form with widgets to collect user information"""
        with st.form("credentials"):
            st.text_input('Username', key='username')
            st.text_input('Password', type='password', key='password')
            st.form_submit_button('Login', on_click=password_entered)

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state['username'] in st.secrets['passwords'] and hmac.compare_digest(st.session_state['password'], st.secrets.passwords[st.session_state['username']]):
            st.session_state['password_correct'] = True
            st.session_state.user = st.session_state['username']
            del st.session_state['password']  # Don't store the password.
        else:
            st.session_state['password_correct'] = False

    # Return True if the username + password is validated.
    if st.session_state.get('password_correct', False):
        return True

    # Show inputs for username + password.
    login_form()
    if "password_correct" in st.session_state:
        st.error('😕 User not known or password incorrect')
    return False

def logout():
    print("logout")
    del st.session_state.password_correct
    del st.session_state.user
    del st.session_state.messages
    st.cache_resource.clear()
    st.cache_data.clear()


##################
### Data Cache ###
##################

# Cache localized strings
@st.cache_data()
def load_localization(locale):
    print("load_localization")
    print(st.session_state)
    # Load in the text bundle and filter by language locale
    df = pd.read_csv("localization.csv")
    df = df.query(f"locale == '{locale}'")
    # Create and return a dictionary of key/values.
    st.session_state.lang_dict = {df.key.to_list()[i]:df.value.to_list()[i] for i in range(len(df.key.to_list()))}
    return st.session_state.lang_dict

# Cache localized strings
@st.cache_data()
def load_rails(username):
    print("load_rails")
    print(st.session_state)
    # Load in the rails bundle and filter by username
    df = pd.read_csv("rails.csv")
    df = df.query(f"username == '{username}'")
    # Create and return a dictionary of key/values.
    rails_dict = {df.key.to_list()[i]:df.value.to_list()[i] for i in range(len(df.key.to_list()))}
    st.session_state.rails = rails_dict
    return st.session_state.rails


#############
### Login ###
#############

def render_ui():
    print("render_ui")
    print(st.session_state)
    # Check for username/password and set the username accordingly
    if not check_password():
        st.stop()  # Do not continue if check_password is not True.

    username = st.session_state.user
    language = st.secrets.languages[username]
    lang_dict = load_localization(language)
    print(st.session_state)
    with st.sidebar:
        load_rails(username)
        load_embedding_model()
        vectorstore = load_vectorstore(username)
        # semantic_cache = load_semantic_cache()
        retriever = load_retriever()
        model = load_llm()
        history = load_chat_history(username)
        memory = load_memory()
        prompt = load_prompt()

    ############
    ### Main ###
    ############

    # Write the welcome text
    try:
        st.markdown(Path(f"""{username}.md""").read_text())
    except:
        st.markdown(Path('welcome.md').read_text())

    # DataStax logo
    with st.sidebar:
        st.image('./assets/datastax-logo.svg')
        st.text('')

    # Logout button
    with st.sidebar:
        with st.form('logout'):
            st.caption(f"""{lang_dict.get('logout_caption', 'Logout')} '{username}'""")
            st.form_submit_button(lang_dict.get('logout_button', 'Logout'), on_click=logout)


    # Include the upload form for new data to be Vectorized
    with st.sidebar:
        with st.form('upload'):
            uploaded_file = st.file_uploader(lang_dict.get('load_context', 'Load Context'), type=['txt', 'pdf'], accept_multiple_files=True)
            submitted = st.form_submit_button(lang_dict.get('load_context_button', 'Load Context'))
            if submitted:
                vectorize_text(uploaded_file)

    # Drop the Conversational Memory
    with st.sidebar:
        with st.form('delete_memory'):
            st.caption(lang_dict.get('delete_memory', 'Delete Memory'))
            submitted = st.form_submit_button(lang_dict.get('delete_memory_button', 'Delete Memory'))
            if submitted:
                with st.spinner(lang_dict.get('deleting_memory', 'Deleting Memory')):
                    memory.clear()

    print(st.session_state)
    # Drop the vector data and start from scratch
    if (username in st.secrets['delete_option'] and st.secrets.delete_option[username] == 'True'):
        with st.sidebar:
            with st.form('delete_context'):
                st.caption(lang_dict.get('delete_context', 'Delete Context'))
                submitted = st.form_submit_button(lang_dict.get('delete_context_button', 'Delete Context'))
                if submitted:
                    with st.spinner(lang_dict.get('deleting_context', 'Deleting Context')):
                        vectorstore.clear()
                        memory.clear()
                        st.session_state.messages = [AIMessage(content=lang_dict.get('assistant_welcome', 'Welcome to the AI Assistant'))]

    # Draw rails
    with st.sidebar:
            st.subheader(lang_dict.get('rails_1', 'Try the following prompts:' ))
            st.caption(lang_dict.get('rails_2', 'copy-paste these to the chat window'))
            for i in st.session_state.rails:
                st.markdown(f"{i}. {st.session_state.rails[i]}")

    # Draw all messages, both user and agent so far (every time the app reruns)
    for message in st.session_state.messages:
        st.chat_message(message.type).markdown(message.content)

    print(st.session_state)
    # Now get a prompt from a user
    if question := st.chat_input(lang_dict.get('assistant_question', 'Ask me a question')):
        print(f"Got question: {question}")

        # Add the prompt to messages, stored in session state
        st.session_state.messages.append(HumanMessage(content=question))

        # Draw the prompt on the page
        print(f"Draw prompt")
        with st.chat_message('human'):
            st.markdown(question)

        # Get the results from Langchain
        print(f"Chat message")
        with st.chat_message('assistant'):
            # UI placeholder to start filling with agent response
            response_placeholder = st.empty()

            history = load_memory().load_memory_variables({})
            print(f"Using memory: {history}")

            inputs = RunnableMap({
                'context': lambda x: retriever.get_relevant_documents(x['question']),
                'chat_history': lambda x: x['chat_history'],
                'question': lambda x: x['question']
            })
            print(f"Using inputs: {inputs}")

            chain = inputs | prompt | model
            print(f"Using chain: {chain}")

            # Call the chain and stream the results into the UI
            response = chain.invoke({'question': question, 'chat_history': history}, config={'callbacks': [StreamHandler(response_placeholder)]})
            print(f"Response: {response}")
            content = response.content

            # Add the result to memory (without the sources)
            memory.save_context({'question': question}, {'answer': content})

            # Write the sources used
            relevant_documents = retriever.get_relevant_documents(question)
            content += f"""
            
*{lang_dict.get('sources_used', 'Sources Used')}*  
"""
            sources = []
            for doc in relevant_documents:
                source = doc.metadata['source']
                page_content = doc.page_content
                if source not in sources:
                    content += f"""📙 :orange[{os.path.basename(os.path.normpath(source))}]  
"""
                    sources.append(source)
            print(f"Used sources: {sources}")
            print(st.session_state)

            # Write the final answer without the cursor
            response_placeholder.markdown(content)

            # Add the answer to the messages session state
            st.session_state.messages.append(AIMessage(content=content))

    with st.sidebar:
                st.caption("v231208.01")