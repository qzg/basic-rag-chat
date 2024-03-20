import streamlit as st
from langchain.prompts import ChatPromptTemplate

# Cache prompt
@st.cache_data()
def load_prompt():
    print("load_prompt")
    template = """You're a helpful AI assistant tasked to answer the user's questions.
You're friendly and you answer extensively with multiple sentences. You prefer to use bulletpoints to summarize.
If you don't know the answer, just say 'I do not know the answer'.

Use the following context to answer the question:
{context}

Use the previous chat history to answer the question:
{chat_history}

Question:
{question}

Answer in the user's language:"""

    return ChatPromptTemplate.from_messages([("system", template)])