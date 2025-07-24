import streamlit as st
import requests
from datetime import datetime
st.set_page_config(page_title="VoltMail History", layout="wide")
st.title(" Sent Email History")
if st.button("🔄 Refresh"):
    st.rerun()
try:
    res = requests.get("http://localhost:5000/api/email-logs")
    logs = res.json()
    if not isinstance(logs, list):
        st.error(" Invalid response from backend.")
    elif not logs:
        st.info("No emails sent yet.")
    else:
        for entry in logs:
            recipient = entry.get('recipientEmail', 'N/A')
            subject = entry.get('subject', 'No Subject')
            company = entry.get('company', 'Unknown')
            role = entry.get('role', 'Unknown')
            product = entry.get('product', 'Unknown')
            timestamp = entry.get('timestamp')
            body = entry.get('body', '')
            time_display = "Unknown"
            if timestamp:
                try:
                    dt = datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S.%fZ")
                    time_display = dt.strftime("%d %b %Y, %I:%M %p")
                except:
                    time_display = timestamp
            st.markdown(f"### 📧 {subject}")
            st.markdown(f"- **To:** `{recipient}`")
            st.markdown(f"- **Company:** {company}")
            st.markdown(f"- **Role:** {role}")
            st.markdown(f"- **Product:** {product}")
            st.markdown(f"- **Sent At:** {time_display}")
            st.text_area("Body", body, height=150, disabled=True)
            st.markdown("---")
except Exception as e:
    st.error(f" Could not fetch email logs: {e}")
