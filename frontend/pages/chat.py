import streamlit as st
from utils.api import send_message
from utils.auth import check_auth, logout
from utils.styles import load_css

st.set_page_config(page_title="AI Chatbot", page_icon="🤖", layout="wide")

load_css()
check_auth()

st.title("🤖 AI Educational Chatbot")

col1, col2 = st.columns([8, 1])

with col2:
    if st.button("Logout"):
        logout()
        st.rerun()


if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


prompt = st.chat_input("Ask anything about your studies...")


if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)


    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = send_message(
                prompt,
                st.session_state.user_id,
                st.session_state.token,
                st.session_state.get("session_id")
            )

            if response.status_code == 200:

                data = response.json()

                answer = data["response"]
                st.session_state.session_id = data["session_id"]

                st.markdown(answer)

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": answer
                    }
                )

            else:
                st.error("Error communicating with AI model")
