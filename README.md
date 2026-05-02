Overview
VoltMail is an advanced cold email platform that combines Retrieval-Augmented Generation (RAG) with comprehensive analytics to craft highly personalized outreach at scale. It leverages LLaMA3 via Groq for lightning-fast inference, ChromaDB for smart context retrieval, and a clean Streamlit dashboard for campaign management.

Features
FeatureDescription AI PersonalizationRAG-powered email generation using LLaMA3 Lightning InferenceGroq integration for real-time generation Smart RetrievalChromaDB vector store with Cohere embeddings Campaign AnalyticsTrack opens, replies, and engagement metrics Campaign ManagementCreate and manage multiple outreach campaigns Multi-ChannelSupports email and LinkedIn outreach

Tech Stack
┌─────────────────────────────────────────────────────┐
│                      VoltMail                       │
├──────────────────────┬──────────────────────────────┤
│      Backend         │         Frontend             │
│  Node.js + Express   │       Streamlit              │
│  MongoDB             │       Plotly                 │
│  Groq API (LLaMA3)   ├──────────────────────────────┤
│  Cohere Embeddings   │          AI / ML             │
│                      │  LangChain (RAG)             │
│                      │  ChromaDB (Vector Store)     │
│                      │  Custom Prompt Engineering   │
└──────────────────────┴──────────────────────────────┘

Getting Started
Prerequisites

Docker & Docker Compose
A Groq API key
A Cohere API key
A MongoDB connection string (local or Atlas)


Installation (Docker — Recommended)
1. Clone the repository
bashgit clone https://github.com/yourusername/voltmail.git
cd voltmail
2. Configure environment variables
bashcp .env.example .env
Open .env and fill in your credentials:
env# API Keys
GROQ_API_KEY=your_groq_api_key
COHERE_API_KEY=your_cohere_api_key

# Database
MONGODB_URI=mongodb://localhost:27017/voltmail

# App
PORT=5000
3. Build and start all services
bashdocker compose up --build
This will spin up:
ServiceURLBackend APIhttp://localhost:5000Frontend Dashboardhttp://localhost:8501
4. Initialize the vector store (first run only)
bashdocker compose exec frontend python -m scripts.init_vectorstore
5. Stop all services
bashdocker compose down

Manual Installation (Without Docker)
<details>
<summary>Click to expand manual setup instructions</summary>
Prerequisites

Node.js v18+
Python 3.10+
MongoDB (local or Atlas)

Backend
bashcd backend
npm install
cp ../.env.example .env   # edit with your credentials
npm start
# API runs at http://localhost:5000
Frontend
bashcd frontend
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r ../requirements.txt
streamlit run app.py
# Dashboard opens at http://localhost:8501
Initialize Vector Store
bashpython -m scripts.init_vectorstore
</details>

Analytics
VoltMail tracks the following engagement metrics out of the box:

Open rates — via pixel tracking
Reply rates — monitored per campaign
Click-through rates — link engagement tracking
Campaign comparison — side-by-side performance views
Timeline analytics — trends over time with Plotly visualizations


Project Structure
voltmail/
├── backend/              # Node.js + Express API
│   ├── routes/
│   ├── models/
│   └── server.js
├── frontend/             # Streamlit dashboard
│   ├── app.py
│   └── scripts/
│       └── init_vectorstore.py
├── docker-compose.yml
├── .env.example
└── requirements.txt

Contributing
Contributions are welcome! Please open an issue first to discuss any changes you'd like to make, then submit a pull request.

Fork the repository
Create a feature branch: git checkout -b feature/my-feature
Commit your changes: git commit -m 'Add my feature'
Push to the branch: git push origin feature/my-feature
Open a pull request


License
This project is licensed under the MIT License.