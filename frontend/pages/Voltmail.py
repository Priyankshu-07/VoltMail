import streamlit as st
import sys, os

# 🔧 Add parent directory to access utils/
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.api_handler import send_email  # 📡 API handler

st.set_page_config(page_title="VoltMail - Cold Email Generator", layout="centered")
st.title("✉️ VoltMail — Cold Email Generator & Sender")
st.markdown("Craft and send high-converting cold emails using AI 🚀")
st.divider()

# 📝 Input Form
with st.form("email_form"):
    st.subheader("📩 Email Details")

    col1, col2 = st.columns(2)
    with col1:
        recipientEmail = st.text_input("📬 Recipient's Email *", placeholder="e.g., ceo@targetcompany.com")
        subject = st.text_input("📌 Email Subject *", placeholder="e.g., Let's collaborate?")
    with col2:
        tone = st.selectbox("🎯 Tone", ["Professional", "Friendly", "Casual"], index=0)
        persona = st.text_input("🧑‍💼 Your Role / Persona", placeholder="e.g., Marketing Lead")

    st.subheader("🏢 About You")
    col3, col4 = st.columns(2)
    with col3:
        companyName = st.text_input("🏢 Company Name", placeholder="e.g., VoltMail Inc.")
    with col4:
        productName = st.text_input("🛠️ Product Name", placeholder="e.g., AI Email Assistant")

    st.subheader("🧠 Context & Strategy")
    userContext = st.text_area("📖 Pitch Context", placeholder="Describe the pain point / your story (optional)")
    customPrompt = st.text_area("🛠️ Custom Prompt (Optional)", placeholder="Tweak tone, include specific phrases...")

    col5, col6 = st.columns(2)
    with col5:
        targetAudience = st.text_input("🎯 Target Audience", placeholder="e.g., SaaS founders")
    with col6:
        emailGoal = st.text_input("🏁 Email Goal", placeholder="e.g., Book a demo")

    submitted = st.form_submit_button("🚀 Generate + Send Email")

# ✅ Send Button Logic
if submitted:
    # 🔐 Only the bare minimum required
    if not recipientEmail or not subject:
        st.error("⚠️ Recipient Email and Subject are required.")
    else:
        with st.spinner("🛠️ Generating & Sending..."):
            final_email = send_email(
                recipientEmail, subject, tone, persona,
                userContext, companyName, productName,
                customPrompt, targetAudience, emailGoal
            )

        # ✅ Display result
        if not final_email or "Error" in final_email or "failed" in final_email.lower():
            st.error("❌ Email generation or sending failed.")
            st.code(final_email)
        else:
            st.success("✅ Email Sent Successfully!")
            st.text_area("📨 Generated Email", value=final_email, height=300, disabled=True)
