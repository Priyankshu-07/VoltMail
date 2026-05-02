# ⚡ VoltMail — AI-Powered Cold Email Platform

VoltMail is a **production-style cold outreach system** that uses **Retrieval-Augmented Generation (RAG)** to generate highly personalized emails at scale, combined with **real-time analytics and campaign tracking**.

It’s not just an email generator — it’s a **full pipeline from lead → personalization → outreach → analytics**.

---

## 🚀 Core Capabilities

### 🧠 AI Personalization Engine
- RAG pipeline using **LLaMA3 (via Groq)**
- Context-aware email generation from vector database
- Dynamic prompt engineering for tone + intent control

### ⚡ Ultra-Fast Inference
- Groq-powered LLaMA3 inference
- Near real-time email generation (<1s latency)

### 🔍 Smart Context Retrieval
- **ChromaDB vector store**
- **Cohere embeddings**
- Retrieves relevant company/user context before generation

### 📬 Campaign Management
- Create and manage multiple outreach campaigns
- Store leads, email history, and responses

### 📊 Analytics Dashboard
- Open tracking (pixel-based)
- Reply tracking
- Engagement metrics per campaign

### 🌐 Multi-Channel Outreach (Planned/Partial)
- Email automation
- LinkedIn personalization pipeline (extensible)

---

## 🧱 Tech Stack

### Backend
- Node.js + Express.js  
- MongoDB (campaigns, logs, analytics)  
- Groq API (LLaMA3 inference)  
- Cohere API (embeddings)

### Frontend
- Streamlit dashboard  
- Plotly (analytics visualizations)

### AI / ML
- LangChain (RAG orchestration)  
- ChromaDB (vector database)  
- Custom prompt pipelines  

---

## 🐳 Dockerized Architecture

The entire system is containerized for **easy deployment and reproducibility**.

### Services
- Backend (Node.js API)
- Frontend (Streamlit UI)
- MongoDB
- Vector DB initialization service

---

## ⚙️ Setup & Installation

### 1. Clone Repository
```bash
git clone https://github.com/yourusername/voltmail.git
cd voltmail
```

---

### 2. Environment Variables

Create a `.env` file in the root:

```env
GROQ_API_KEY=your_key
COHERE_API_KEY=your_key
MONGO_URI=your_mongo_uri
```

---

## 🐳 Run with Docker (Recommended)

### Build and start all services
```bash
docker-compose up --build
```

### Services will be available at:
- Backend → http://localhost:5000  
- Frontend → http://localhost:8501  

---

## 🧪 Local Development (Without Docker)

### Backend
```bash
cd backend
npm install
npm start
```

---

### Frontend
```bash
cd frontend
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r ../requirements.txt

streamlit run app.py
```

---

### Initialize Vector Store
```bash
python -m scripts.init_vectorstore
```

---

## 📊 Analytics Tracked

- Email open rates (pixel tracking)
- Reply rates
- Campaign-level engagement
- Lead-level interaction logs

---

## 🧠 System Architecture (High-Level Flow)

```
Lead Input → Embedding → Vector Search (ChromaDB)
          → Context Retrieval → Prompt Engineering
          → LLaMA3 (Groq) → Email Generation
          → Campaign Tracking → Analytics Dashboard
```

---

## 📌 Why This Project Matters

Most “AI email generators” are just wrappers.

VoltMail goes further:
- Implements **RAG pipeline (real AI system design)**
- Handles **data storage + retrieval**
- Includes **analytics + tracking layer**
- Designed like a **real SaaS backend**

---

## 🔮 Future Improvements

- Email sending integration (Gmail API / SendGrid)
- A/B testing for subject lines
- Automated follow-ups
- Lead scraping + enrichment
- Authentication & multi-user support

---

## ⚠️ Reality Check

This is **not a deep ML research project** — it’s a **systems + AI integration project**.

That’s actually a strength:
- Shows **engineering thinking**
- Shows **real-world architecture**
- Relevant for **SDE + AI Engineer roles**