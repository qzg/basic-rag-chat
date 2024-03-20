import streamlit as st
import providers.azure_openai as provider

# Cache OpenAI Embedding for future runs
@st.cache_resource(show_spinner=st.session_state.lang_dict.get('load_embedding', 'Loading Embedding'))
def load_embedding_model():
    print("load_embedding_model")
    # Get the OpenAI Embedding
    return provider.load_embedding_model()


# Cache OpenAI Chat Model for future runs
@st.cache_resource(show_spinner=st.session_state.lang_dict.get('load_model', 'Loading Model'))
def load_llm():
    print("load_llm")
    return provider.load_llm()

