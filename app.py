import streamlit as st
from main import analyze_document

st.set_page_config(
    page_title="Thread Chatbot",
    page_icon="💬",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.title("Thread Chatbot")
st.markdown("""
This application analyzes documents and answers questions based on their content.
It sequentially searches through sales, HR, finance, and marketing documents to find relevant information.
""")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Ask me anything about your documents..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = analyze_document(prompt)
            st.markdown(response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
