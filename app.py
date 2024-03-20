import streamlit as st


#####################
### Configuration #
#####################

# Define the number of docs to retrieve from the vectorstore and memory
st.session_state.top_k_vectorstore = 4
st.session_state.top_k_memory = 3
st.session_state.lang_dict = {}

from ui import init_ui, render_ui

print("Started")

init_ui()
render_ui()
