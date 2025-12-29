import streamlit as st
import pandas as pd
from loginBacked import add_user 

def login_ui():
    if 'logged_in' not in st.session_state:
     st.header("Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        check_password(username, password)


def signup_ui():
   if 'logged_in' not in st.session_state:
     st.header("Signup Page")
     new_username = st.text_input("Choose a Username")
     new_password = st.text_input("Choose a Password", type="password")
     
   if st.button("Sign Up"):
            add_user(new_username,new_password)


def login_completed_sidebar():
    st.sidebar.title("You are logged in.")
    page = st.sidebar.radio("Go to", ["Home",  "Logout"])
    st.session_state.current_page = page

def login_not_completed_sidebar():
    st.sidebar.title("Please log in to access the app features.")
    page=st.sidebar.radio("Welcome", ["login", "signup"])
    st.session_state.current_page = page