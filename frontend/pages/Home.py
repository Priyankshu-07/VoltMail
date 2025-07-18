import streamlit as st

st.title("🏠 Welcome to VoltMail")
st.markdown("""
VoltMail helps you:

- Generate personalized cold emails using AI (Groq + ChromaDB)
- Use your own custom context to tailor the message
- Save logs to MongoDB
- Analyze email generation history

🔌 Built using Fast, Modern Stack:
- Streamlit Frontend
- Express + MongoDB Backend
- ChromaDB + LangChain + Groq API

Click **VoltMail** on the sidebar to start!
""")
