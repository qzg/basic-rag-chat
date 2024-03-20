import tempfile, os
import streamlit as st

from langchain.globals import set_llm_cache
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.cache import AstraDBSemanticCache
from langchain.memory import AstraDBChatMessageHistory, ConversationBufferWindowMemory

from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import AstraDB

from models import load_embedding_model 



# Function for Vectorizing uploaded data into Astra DB
def vectorize_text(uploaded_files):
    print("vectorize_text")
    for uploaded_file in uploaded_files:
        if uploaded_file is not None:
            
            # Write to temporary file
            temp_dir = tempfile.TemporaryDirectory()
            file = uploaded_file
            print(f"""Processing: {file}""")
            temp_filepath = os.path.join(temp_dir.name, file.name)
            with open(temp_filepath, 'wb') as f:
                f.write(file.getvalue())

            # Create the text splitter
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size = 1500,
                chunk_overlap  = 100
            )

            if uploaded_file.name.endswith('txt'):
                file = [uploaded_file.read().decode()]
                texts = text_splitter.create_documents(file, [{'source': uploaded_file.name}])
                load_vectorstore(st.session_state.user).add_documents(texts)
                st.info(f"{len(texts)} {st.session_state.lang_dict.get('load_text', 'Texts')}")

            if uploaded_file.name.endswith('pdf'):
                # Read PDF
                docs = []
                loader = PyPDFLoader(temp_filepath)
                docs.extend(loader.load())

                pages = text_splitter.split_documents(docs)
                load_vectorstore(st.session_state.user).add_documents(pages)  
                st.info(f"{len(pages)} {st.session_state.lang_dict.get('load_pdf', 'PDF Pages')}")


@st.cache_resource(show_spinner=st.session_state.lang_dict.get('load_retriever', 'Loading Retriever'))
def load_semantic_cache():
    print("load_semantic_cache")
    set_llm_cache(
        AstraDBSemanticCache(
            api_endpoint=os.environ["ASTRA_ENDPOINT"],
            token=st.secrets["ASTRA_TOKEN"],
            embedding=load_embedding_model(),
            collection_name="demo_semantic_cache",
        )
    )
    
# Cache Retriever for future runs
@st.cache_resource(show_spinner=st.session_state.lang_dict.get('load_retriever', 'Loading Retriever'))
def load_retriever():
    print("load_retriever")
    # Get the Retriever from the Vectorstore
    return load_vectorstore(st.session_state.user).as_retriever(
        search_kwargs={"k": st.session_state.top_k_vectorstore}
    )


# Cache Vector Store for future runs
@st.cache_resource(show_spinner=st.session_state.lang_dict.get('load_vectorstore', 'Loading Vector Store'))
def load_vectorstore(username):
    print("load_vectorstore")
    # Get the load_vectorstore store from Astra DB
    return AstraDB(
        embedding=load_embedding_model(),
        collection_name=f"vector_context_{username}",
        token=st.secrets["ASTRA_TOKEN"],
        api_endpoint=os.environ["ASTRA_ENDPOINT"],
    )


# Cache Chat History for future runs
@st.cache_resource(show_spinner=st.session_state.lang_dict.get('load_message_history', 'Loading Message History'))
def load_chat_history(username):
    print(f"load_chat_history for {username}_{st.session_state.session_id}")
    return AstraDBChatMessageHistory(
        session_id=f"{username}_{st.session_state.session_id}",
        api_endpoint=os.environ["ASTRA_ENDPOINT"],
        token=st.secrets["ASTRA_TOKEN"],
    )

@st.cache_resource(show_spinner=st.session_state.lang_dict.get('load_message_history', 'Loading Message History'))
def load_memory():
    print("load_memory")
    return ConversationBufferWindowMemory(
        chat_memory=load_chat_history(st.session_state.user),
        return_messages=True,
        k=st.session_state.top_k_memory,
        memory_key="chat_history",
        input_key="question",
        output_key='answer',
    )
