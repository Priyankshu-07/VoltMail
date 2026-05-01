import streamlit as st
import requests
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta
import os

st.set_page_config(page_title="VoltMail Analytics", layout="wide", initial_sidebar_state="collapsed")
st.markdown("""
<style>
    .metric-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .metric-box h3 {
        margin: 0;
        font-size: 2rem;
        font-weight: bold;
    }
    .metric-box p {
        margin: 0.5rem 0 0 0;
        opacity: 0.9;
    }
    .email-card {
        background: #f8f9fa;
        border: 1px solid #e9ecef;
        border-radius: 8px;
        padding: 1rem;
        margin: 0.5rem 0;
        border-left: 4px solid #667eea;
    }
    .email-meta {
        color: #6c757d;
        font-size: 0.9rem;
        margin-top: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

st.title("VoltMail Dashboard")
st.markdown("Track your email campaigns and outreach performance")

col1, col2, col3 = st.columns([1, 1, 8])
with col1:
    if st.button("Refresh", type="primary"):
        st.rerun()

@st.cache_data(ttl=60)
def fetch_email_logs():
    try:
        backend_url = os.getenv("BACKEND_URL", "http://backend:5000")
        response = requests.get(f"{backend_url}/api/email-logs")
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Failed to fetch data: {response.status_code}")
            return []
    except Exception as e:
        st.error(f"Could not connect to backend: {e}")
        return []

logs = fetch_email_logs()
if not logs:
    st.warning("No email data found. Start sending emails to see analytics!")
    st.stop()

df = pd.DataFrame(logs)
if 'timestamp' in df.columns:
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['date'] = df['timestamp'].dt.date

st.markdown("---")
st.subheader("Overview")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown(f"""
    <div class="metric-box">
        <h3>{len(df)}</h3>
        <p>Total Emails</p>
    </div>
    """, unsafe_allow_html=True)
with col2:
    unique_recipients = df['recipientEmail'].nunique()
    st.markdown(f"""
    <div class="metric-box">
        <h3>{unique_recipients}</h3>
        <p>Recipients</p>
    </div>
    """, unsafe_allow_html=True)
with col3:
    unique_companies = df['company'].nunique()
    st.markdown(f"""
    <div class="metric-box">
        <h3>{unique_companies}</h3>
        <p>Companies</p>
    </div>
    """, unsafe_allow_html=True)
with col4:
    if len(df) > 0:
        days_active = (df['timestamp'].max() - df['timestamp'].min()).days + 1
        avg_per_day = len(df) / max(1, days_active)
        st.markdown(f"""
        <div class="metric-box">
            <h3>{avg_per_day:.1f}</h3>
            <p>Per Day</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")
col1, col2 = st.columns(2)
with col1:
    st.subheader("Daily Activity")
    if 'date' in df.columns:
        daily_counts = df.groupby('date').size().reset_index(name='emails')
        daily_counts['date'] = pd.to_datetime(daily_counts['date'])
        fig = px.bar(daily_counts, x='date', y='emails', color='emails', color_continuous_scale="Blues")
        fig.update_layout(showlegend=False, height=300, margin=dict(l=0, r=0, t=0, b=0))
        st.plotly_chart(fig, use_container_width=True)
with col2:
    st.subheader("Top Companies")
    company_counts = df['company'].value_counts().head(8)
    fig = px.pie(values=company_counts.values, names=company_counts.index, color_discrete_sequence=px.colors.qualitative.Set3)
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(height=300, margin=dict(l=0, r=0, t=0, b=0))
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.subheader("Recent Emails")
search = st.text_input("Search emails", placeholder="Search by recipient, company, or subject...")
filtered_df = df.copy()
if search:
    mask = (
        filtered_df['recipientEmail'].str.contains(search, case=False, na=False) |
        filtered_df['company'].str.contains(search, case=False, na=False) |
        filtered_df['subject'].str.contains(search, case=False, na=False)
    )
    filtered_df = filtered_df[mask]

filtered_df = filtered_df.sort_values('timestamp', ascending=False)
if len(filtered_df) == 0:
    st.info("No emails match your search.")
else:
    st.write(f"Showing {len(filtered_df)} emails")
    for _, email in filtered_df.head(20).iterrows():
        time_str = "Unknown time"
        if pd.notna(email['timestamp']):
            time_str = email['timestamp'].strftime("%b %d, %Y at %I:%M %p")
        st.markdown(f"""
        <div class="email-card">
            <strong>{email.get('subject', 'No Subject')}</strong><br>
            <strong>To:</strong> {email.get('recipientEmail', 'N/A')}<br>
            <strong>Company:</strong> {email.get('company', 'Unknown')} • 
            <strong>Role:</strong> {email.get('role', 'Unknown')}<br>
            <div class="email-meta">
                {time_str}
            </div>
        </div>
        """, unsafe_allow_html=True)

        if pd.notna(email.get('body')):
            with st.expander("View Email Content"):
                st.text_area("Email Body:", value=email['body'], height=150, disabled=True, key=f"body_{email.name}")

st.markdown("---")
st.markdown("Use the search box to quickly find specific emails or companies")