import streamlit as st
from utils.styles import load_css

st.set_page_config(
    page_title="AI Education Platform",
    page_icon="🎓",
    layout="wide"
)

load_css()

st.markdown(
    """
    <div class="hero">
        <h1>🎓 Personalized Education Platform</h1>
        <p>AI-Powered Chatbot for Student Support</p>
    </div>
    """,
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div class="feature-card">
            <h3>🤖 AI Chatbot</h3>
            <p>Ask educational questions and receive personalized recommendations.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div class="feature-card">
            <h3>📚 Smart Recommendations</h3>
            <p>Get courses and learning materials based on your needs.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        """
        <div class="feature-card">
            <h3>📈 Progress Tracking</h3>
            <p>Track your learning journey with analytics dashboard.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

st.divider()

st.subheader("🚀 Platform Features")

st.write("✔ User Authentication")
st.write("✔ AI-Powered Educational Assistant")
st.write("✔ Personalized Learning Recommendations")
st.write("✔ Student Dashboard")
st.write("✔ FastAPI + Streamlit Integration")
st.write("✔ RAG Pipeline Integration")

st.info("Use the sidebar to navigate between pages.")