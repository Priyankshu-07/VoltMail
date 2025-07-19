import streamlit as st
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.api_handler import send_email 
st.set_page_config(page_title="VoltMail - Cold Email Generator", layout="centered")
st.title(" VoltMail — Cold Email Generator & Sender")
st.markdown("Craft and send high-converting cold emails using AI ")
st.divider()
def initialize_session_state():
    default_values = {
        'recipient_email': '',
        'email_subject': '',
        'email_tone': 'Professional',
        'user_persona': '',
        'company_name': '',
        'product_name': '',
        'user_context': '',
        'custom_prompt': '',
        'target_audience': '',
        'email_goal': '',
        'generated_email': '',
        'email_sent': False
    }    
    for key, default_value in default_values.items():
        if key not in st.session_state:
            st.session_state[key] = default_value
initialize_session_state()
with st.form("email_form"):
    st.subheader(" Email Details")
    
    col1, col2 = st.columns(2)
    with col1:
        recipientEmail = st.text_input(
            " Recipient's Email *", 
            value=st.session_state.recipient_email,
            placeholder="e.g., ceo@targetcompany.com"
        )
        subject = st.text_input(
            " Email Subject *", 
            value=st.session_state.email_subject,
            placeholder="e.g., Let's collaborate?"
        )
    with col2:
        tone = st.selectbox(
            " Tone", 
            ["Professional", "Friendly", "Casual"], 
            index=["Professional", "Friendly", "Casual"].index(st.session_state.email_tone)
        )
        persona = st.text_input(
            " Your Role / Persona", 
            value=st.session_state.user_persona,
            placeholder="e.g., Marketing Lead"
        )
    
    st.subheader(" About You")
    col3, col4 = st.columns(2)
    with col3:
        companyName = st.text_input(
            " Company Name", 
            value=st.session_state.company_name,
            placeholder="e.g., VoltMail Inc."
        )
    with col4:
        productName = st.text_input(
            " Product Name", 
            value=st.session_state.product_name,
            placeholder="e.g., AI Email Assistant"
        ) 
    st.subheader(" Context & Strategy")
    userContext = st.text_area(
        " Pitch Context", 
        value=st.session_state.user_context,
        placeholder="Describe the pain point / your story (optional)"
    )
    customPrompt = st.text_area(
        " Custom Prompt (Optional)", 
        value=st.session_state.custom_prompt,
        placeholder="Tweak tone, include specific phrases..."
    ) 
    col5, col6 = st.columns(2)
    with col5:
        targetAudience = st.text_input(
            "🎯 Target Audience", 
            value=st.session_state.target_audience,
            placeholder="e.g., SaaS founders"
        )
    with col6:
        emailGoal = st.text_input(
            " Email Goal", 
            value=st.session_state.email_goal,
            placeholder="e.g., Book a demo"
        )
    
    submitted = st.form_submit_button(" Generate + Send Email")
    if submitted:
        st.session_state.recipient_email = recipientEmail
        st.session_state.email_subject = subject
        st.session_state.email_tone = tone
        st.session_state.user_persona = persona
        st.session_state.company_name = companyName
        st.session_state.product_name = productName
        st.session_state.user_context = userContext
        st.session_state.custom_prompt = customPrompt
        st.session_state.target_audience = targetAudience
        st.session_state.email_goal = emailGoal
if submitted:
    if not recipientEmail or not subject:
        st.error("Recipient Email and Subject are required.")
    else:
        with st.spinner(" Generating & Sending..."):
            final_email = send_email(
                recipientEmail, subject, tone, persona,
                userContext, companyName, productName,
                customPrompt, targetAudience, emailGoal
            )
        st.session_state.generated_email = final_email 
        if not final_email or "Error" in final_email or "failed" in final_email.lower():
            st.error(" Email generation or sending failed.")
            st.code(final_email)
            st.session_state.email_sent = False
        else:
            st.success(" Email Sent Successfully!")
            st.session_state.email_sent = True
if st.session_state.generated_email and st.session_state.email_sent:
    st.subheader(" Last Generated Email")
    st.text_area(
        "Generated Email", 
        value=st.session_state.generated_email, 
        height=300, 
        disabled=True,
        key="display_email"
    )
st.divider()
col_clear, col_info = st.columns([1, 3])
with col_clear:
    if st.button(" Clear All Data"):
        for key in st.session_state.keys():
            if key.startswith(('recipient_', 'email_', 'user_', 'company_', 'product_', 'target_', 'custom_', 'generated_')):
                del st.session_state[key]
        st.rerun()
with col_info:
    st.caption(" Your data is preserved across page reloads. Click 'Clear All Data' to reset the form.")