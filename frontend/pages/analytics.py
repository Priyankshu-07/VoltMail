import streamlit as st
import requests

st.title("📊 Email Analytics Dashboard")

try:
    res = requests.get("http://localhost:5000/api/email-logs")
    logs = res.json().get("logs", [])

    if not logs:
        st.warning("No email logs found.")
    else:
        for entry in logs:
            st.markdown("---")
            st.markdown(f"**To:** {entry.get('name')} at {entry.get('company')}")
            st.markdown(f"**Role:** {entry.get('role')} | **Product:** {entry.get('product')}")
            st.text_area("Generated Email", entry.get("email"), height=200)
except Exception as e:
    st.error(f"Failed to load logs: {e}")
