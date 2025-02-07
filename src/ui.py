import streamlit as st

def display_chat():
    """Streamlit UI for chatbot."""
    st.title("💊 Medicine Chatbot")
    st.write("Ask me anything about medicines! sm on")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
