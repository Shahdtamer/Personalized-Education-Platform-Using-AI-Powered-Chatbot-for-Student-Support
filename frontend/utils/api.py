import requests
import streamlit as st

BASE_URL = "http://127.0.0.1:8000"


def login_user(email, password):
    url = f"{BASE_URL}/auth/login"

    payload = {
        "email": email,
        "password": password
    }

    response = requests.post(url, json=payload)
    return response



def signup_user(name, email, password):
    url = f"{BASE_URL}/auth/register"

    payload = {
        "full_name": name,
        "email": email,
        "password": password
    }

    response = requests.post(url, json=payload)
    return response



def send_message(message, user_id, token, session_id=None):
    url = f"{BASE_URL}/chat/"

    headers = {
        "Authorization": f"Bearer {token}"
    }

    payload = {
        "message": message,
        "user_id": user_id,
        "session_id": session_id
    }

    response = requests.post(url, json=payload, headers=headers)
    return response

