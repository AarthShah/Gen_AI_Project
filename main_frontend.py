import streamlit as st
from loginUI import *
from Welcome_Home_UI import home_page

st.set_page_config(page_title="Risey AI" ,page_icon="https://png.pngtree.com/png-clipart/20250307/original/pngtree-technology-focused-ai-chatbot-logo-png-image_20593070.png")

def change_page_status(status):
    st.session_state.current_page=status


if "current_page" not in st.session_state:
    st.session_state.current_page="Login"

if "login_status" not in st.session_state:
    st.session_state.login_status=False

if "username" not in st.session_state:
    st.session_state.username=None

if "welcome_message_status" not in st.session_state:
    st.session_state.welcome_message_status=False

if st.session_state.login_status==False:  
    if st.session_state.current_page=="Login":
        start_message()
        login_ui()
        
    if st.session_state.current_page=="Signup":
        start_message("Signup")
        signup_ui()

else:
    page=st.session_state.current_page=login_completed_sidebar()
    if page=="Chat":
        if st.session_state.welcome_message_status==False:
            message=home_page()
            




