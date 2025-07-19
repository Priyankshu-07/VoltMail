import streamlit as st
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    .main-header {
        text-align: center;
        padding: 3rem 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 20px;
        margin-bottom: 3rem;
        color: white;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }
    
    .hero-title {
        font-family: 'Inter', sans-serif;
        font-size: 3.5rem;
        font-weight: 700;
        margin-bottom: 1rem;
        background: linear-gradient(45deg, #ffffff, #e0e7ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .hero-subtitle {
        font-size: 1.3rem;
        font-weight: 400;
        opacity: 0.9;
        max-width: 600px;
        margin: 0 auto;
    }
    
    .feature-card {
        background: white;
        padding: 2.5rem;
        border-radius: 15px;
        box-shadow: 0 5px 20px rgba(0,0,0,0.08);
        border: 1px solid #f0f0f0;
        height: 100%;
        transition: all 0.3s ease;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(0,0,0,0.15);
    }
    
    .feature-title {
        font-family: 'Inter', sans-serif;
        font-size: 1.4rem;
        font-weight: 600;
        margin-bottom: 1rem;
        color: #2d3748;
    }
    
    .feature-description {
        color: #4a5568;
        line-height: 1.6;
        font-size: 1rem;
    }
    
    .tech-stack {
        background: linear-gradient(135deg, #f7fafc 0%, #edf2f7 100%);
        border-radius: 15px;
        padding: 2.5rem;
        margin: 3rem 0;
        text-align: center;
    }
    
    .tech-item {
        background: white;
        padding: 0.8rem 1.5rem;
        border-radius: 10px;
        margin: 0.5rem;
        display: inline-block;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        border: 1px solid #e2e8f0;
        font-weight: 500;
        color: #4a5568;
        transition: all 0.2s ease;
    }
    
    .tech-item:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }
    
    .cta-section {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        border-radius: 20px;
        padding: 3rem;
        text-align: center;
        color: white;
        margin: 3rem 0;
        box-shadow: 0 10px 30px rgba(79, 172, 254, 0.3);
    }
    
    .benefits-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 2rem;
        margin: 2rem 0;
    }
    
    .benefit-item {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        border-left: 4px solid #667eea;
        box-shadow: 0 3px 15px rgba(0,0,0,0.08);
    }
    
    .benefit-title {
        font-weight: 600;
        color: #2d3748;
        margin-bottom: 0.5rem;
    }
    
    .benefit-text {
        color: #4a5568;
        line-height: 1.5;
    }
    
    @media (max-width: 768px) {
        .hero-title { font-size: 2.5rem; }
        .hero-subtitle { font-size: 1.1rem; }
        .main-header { padding: 2rem 1rem; }
        .feature-card { padding: 2rem; }
        .cta-section { padding: 2rem; }
    }
</style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="main-header">
    <div class="hero-title">VoltMail</div>
    <div class="hero-subtitle">
        AI-powered cold email generation platform that creates personalized, high-converting outreach emails in seconds
    </div>
</div>
""", unsafe_allow_html=True)

# Features Section
st.markdown("## Core Features")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-title">AI Email Generation</div>
        <div class="feature-description">
            Advanced AI analyzes your context and generates personalized cold emails that drive results.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-title">Smart Personalization</div>
        <div class="feature-description">
            ChromaDB vector search matches your content with prospect data for maximum relevance.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-title">Performance Analytics</div>
        <div class="feature-description">
            Track and analyze your email campaigns with detailed logging and insights.
        </div>
    </div>
    """, unsafe_allow_html=True)
st.markdown("## Why VoltMail?")
st.markdown("""
<div class="benefits-grid">
    <div class="benefit-item">
        <div class="benefit-title">Save Time</div>
        <div class="benefit-text">Generate professional emails in seconds instead of hours</div>
    </div>
    <div class="benefit-item">
        <div class="benefit-title">Higher Response Rates</div>
        <div class="benefit-text">AI personalization increases engagement and replies</div>
    </div>
    <div class="benefit-item">
        <div class="benefit-title">Easy to Use</div>
        <div class="benefit-text">Intuitive interface requires no technical expertise</div>
    </div>
    <div class="benefit-item">
        <div class="benefit-title">Scalable Solution</div>
        <div class="benefit-text">Handle high-volume outreach with consistent quality</div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="tech-stack">
    <h3 style="color: #2d3748; margin-bottom: 1.5rem;">Built with Modern Technology</h3>
    <span class="tech-item">Streamlit</span>
    <span class="tech-item">Express.js</span>
    <span class="tech-item">MongoDB</span>
    <span class="tech-item">Groq AI</span>
    <span class="tech-item">ChromaDB</span>
    <span class="tech-item">LangChain</span>
</div>
""", unsafe_allow_html=True)

# Call to Action
st.markdown("""
<div class="cta-section">
    <h2 style="margin-bottom: 1rem;">Ready to Get Started?</h2>
    <p style="font-size: 1.1rem; opacity: 0.9; margin-bottom: 1.5rem;">
        Click <strong>VoltMail</strong> in the sidebar to begin generating your first AI-powered cold email.
    </p>
</div>
""", unsafe_allow_html=True)
