import streamlit as st
from Agent  import chat_model

def chat_screen():
    input=st.chat_input("You: ", key="input_message")
    if input:
        response=chat_model(input)
        st.chat_message("ai").write(response)

def first_chat_message(message):
    if message:
        st.chat_message("user").write(message)
        response=chat_model(message)
        st.chat_message("ai").write(response)