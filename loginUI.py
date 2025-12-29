import streamlit as st
import pandas as pd
from loginBacked import add_user ,check_password
import time

def login_ui():
    st.header("Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    col1,col2,col3=st.columns([1,6,1])
    with col1:
        if st.button("Login"):
            message=check_password(username, password)
            if message=="Login Successful!":
                 with col2:
                    st.success(message)
                    time.sleep(1)
                    st.rerun()
            else:
                 with col2:
                    st.error(message)
                    time.sleep(3)
                    st.rerun()
            return username
    with col3:
        if st.button("Sign Up"):
            st.session_state.current_page = "Signup"
            st.rerun()




def signup_ui():
        st.header("Signup Page")
        new_username1 = st.text_input("Choose a Username")
        new_password1 = st.text_input("Choose a Password", type="password")
        if st.button("Resgister"):
                add_user(new_username1,new_password1)
                st.session_state.current_page ="Login"
                time.sleep(2)
                st.rerun()
        


def login_completed_sidebar():
    st.sidebar.title("You are logged in.")
    page = st.sidebar.radio("# Go to", ["Chat",  "Logout"])
    return page

# def login_not_completed_sidebar():
#     st.sidebar.title("Please log in to access the app features.")
#     page=st.sidebar.radio("Welcome", ["Login", "Signup"])
#     return page

def start_message(option="LOGIN"):
    col1,col2=st.columns([1,7])
    with col1 :
        st.image("https://png.pngtree.com/png-clipart/20250307/original/pngtree-technology-focused-ai-chatbot-logo-png-image_20593070.png",width=100)

    with col2:
        st.title(f"{option} TO RISEY AI...^_^",text_alignment="left")



