import streamlit as st


def load_css():
    st.markdown(
        """
        <style>
        .main {
            background-color: #0f172a;
            color: white;
        }

        .hero {
            padding: 2rem;
            border-radius: 20px;
            background: linear-gradient(to right, #2563eb, #7c3aed);
            color: white;
            text-align: center;
            margin-bottom: 2rem;
        }

        .feature-card {
            padding: 1rem;
            border-radius: 16px;
            background-color: #1e293b;
            margin-bottom: 1rem;
        }

        .stButton>button {
            width: 100%;
            border-radius: 12px;
            height: 3em;
            background-color: #2563eb;
            color: white;
            font-size: 16px;
            border: none;
        }

        .chat-box {
            background-color: #1e293b;
            padding: 1rem;
            border-radius: 12px;
            margin-bottom: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )