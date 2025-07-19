import streamlit as st
st.set_page_config(
    page_title="VoltMail",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.sidebar.title("⚡ VoltMail")
st.sidebar.markdown("###  Navigation")
st.sidebar.markdown("---")
st.sidebar.markdown(" *Cold email generator powered by AI, ChromaDB & Groq.*")
st.markdown("""
    <style>
        .centered-title {
            text-align: center;
            font-size: 3rem;
            color: #1a73e8;
        }
        .centered-subtitle {
            text-align: center;
            font-size: 1.5rem;
            color: #333333;
        }
        .centered-desc {
            text-align: center;
            font-size: 1rem;
            color: #555;
            margin-top: 10px;
        }
    </style>

    <h1 class="centered-title">⚡ VoltMail</h1>
    <h3 class="centered-subtitle">AI-Powered Cold Email Generator</h3>
    <p class="centered-desc">Use the sidebar to start generating emails or explore your email analytics.</p>
""", unsafe_allow_html=True)
