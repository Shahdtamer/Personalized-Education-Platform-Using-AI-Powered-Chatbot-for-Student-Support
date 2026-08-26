import streamlit as st
from utils.api import login_user, signup_user
from utils.styles import load_css

st.set_page_config(page_title="Login", page_icon="🔐")

load_css()

st.title("🔐 Authentication")

menu = ["Login", "Sign Up"]
choice = st.selectbox("Select Option", menu)


if choice == "Login":

    st.subheader("Login to Your Account")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        response = login_user(email, password)

        if response.status_code == 200:
            data = response.json()

            st.session_state.token = data["access_token"]
            st.session_state.user = email
            st.session_state.user_id = data["user_id"]

            st.success("Login Successful")

        else:
            st.error("Invalid Email or Password")


if choice == "Sign Up":

    st.subheader("Create New Account")

    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    password = st.text_input("Password", type="password")

    if st.button("Create Account"):

        response = signup_user(name, email, password)

        if response.status_code == 200:
            st.success("Account Created Successfully")

        else:
            st.error("Error Creating Account")