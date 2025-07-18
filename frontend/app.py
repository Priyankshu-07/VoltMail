import streamlit as st

# Page configuration
st.set_page_config(
    page_title="VoltMail",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar
st.sidebar.title("VoltMail ⚡")
st.sidebar.markdown("## Navigation")
st.sidebar.markdown("""
- 🏠 Home  
- ✍️ VoltMail  
- 📊 Dashboard
""")
st.sidebar.markdown("---")
st.sidebar.markdown("Cold email generator powered by AI, ChromaDB, and Groq.")

# Main welcome screen
st.markdown("""
    <h1 style='text-align: center;'>⚡ VoltMail</h1>
    <h3 style='text-align: center;'>AI-Powered Cold Email Generator</h3>
    <p style='text-align: center;'>Use the sidebar to start generating emails or view analytics.</p>
""", unsafe_allow_html=True)
