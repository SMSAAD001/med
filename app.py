import streamlit as st
from src.chatbot import get_response
from src.ui import display_chat

display_chat()

if user_input := st.chat_input("Type your query..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    bot_reply = get_response(user_input)
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})

    with st.chat_message("assistant"):
        st.markdown(bot_reply)
