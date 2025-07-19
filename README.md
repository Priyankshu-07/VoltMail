
# VoltMail: AI-Powered Cold Email Generator


VoltMail is an advanced cold email platform that combines Retrieval-Augmented Generation (RAG) with comprehensive analytics to create highly personalized outreach campaigns at scale.

##  Key Features

- **AI-Powered Personalization**: Generate tailored emails using RAG with LLaMA3
- **Lightning Fast Inference**: Groq integration for real-time email generation
- **Smart Context Retrieval**: ChromaDB vector store with Cohere embeddings
- **Campaign Management**: Create and track multiple outreach campaigns
- **Comprehensive Analytics**: Track opens, replies, and engagement metrics
- **Multi-Channel Outreach**: Supports email and LinkedIn integration

##  Technology Stack

**Backend**:
- Node.js + Express.js
- MongoDB (Data persistence)
- Groq API (LLaMA3 inference)
- Cohere (Embeddings)

**Frontend**:
- Streamlit (Dashboard)
- Plotly (Visualizations)

**AI/ML**:
- LangChain (RAG orchestration)
- ChromaDB (Vector storage)
- Custom prompt engineering


## 🛠️ Installation

### Prerequisites
- Node.js v18+
- Python 3.10+
- MongoDB (local or Atlas)
- Groq API key
- Cohere API key

### Setup Instructions

1. **Clone repository**
   ```bash
   git clone https://github.com/yourusername/voltmail.git
   cd voltmail
Backend setup

bash
cd backend
npm install
cp ../.env.example .env
# Edit .env with your credentials
Frontend setup

bash
cd ../frontend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r ../requirements.txt
Initialize vectorstore

bash
python -m scripts.init_vectorstore
 Running the Application
Start backend service

bash
cd backend
npm start
# API will run on http://localhost:5000
Launch frontend dashboard

bash
cd ../frontend
streamlit run app.py
# UI will open at http://localhost:8501
📊 Analytics Metrics Tracked
Open rates (via pixel tracking)

