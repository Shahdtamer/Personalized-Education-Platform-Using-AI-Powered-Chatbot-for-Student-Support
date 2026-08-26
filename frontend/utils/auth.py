import streamlit as st
def check_auth():
    if "token" not in st.session_state:
        st.warning("Please login first")
        st.stop()
def logout():
    st.session_state.clear()

