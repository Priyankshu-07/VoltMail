
# VoltMail: AI-Powered Cold Email Generator


VoltMail is an advanced cold email platform that combines Retrieval-Augmented Generation (RAG) with comprehensive analytics to create highly personalized outreach campaigns at scale.

## ✨ Key Features

- **AI-Powered Personalization**: Generate tailored emails using RAG with LLaMA3
- **Lightning Fast Inference**: Groq integration for real-time email generation
- **Smart Context Retrieval**: ChromaDB vector store with Cohere embeddings
- **Campaign Management**: Create and track multiple outreach campaigns
- **Comprehensive Analytics**: Track opens, replies, and engagement metrics
- **Multi-Channel Outreach**: Supports email and LinkedIn integration

## 🚀 Technology Stack

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

## 📂 Project Structure
voltmail/
├── backend/ # Backend services
│ ├── config/ # Configuration files
│ │ └── database.js # DB connection setup
│ ├── controllers/ # Business logic
│ │ ├── campaign.js # Campaign management
│ │ ├── email.js # Email generation
│ │ └── analytics.js # Analytics data
│ ├── models/ # Database models
│ │ ├── Campaign.js # Campaign schema
│ │ └── EmailLog.js # Email tracking
│ ├── routes/ # API endpoints
│ │ └── api/ # Versioned API routes
│ ├── services/ # External services
│ │ ├── llm/ # LLM integrations
│ │ ├── email/ # Email providers
│ │ └── vectorstore/ # Vector DB operations
│ └── server.js # Entry point
│
├── frontend/ # User interface
│ ├── assets/ # Static files
│ ├── components/ # Reusable UI components
│ ├── pages/ # Application views
│ │ ├── 1_🏠_Home.py # Main dashboard
│ │ ├── 2_📧_Compose.py # Email creation
│ │ └── 3_📊_Analytics.py # Metrics
│ ├── utils/ # Helper functions
│ └── app.py # Streamlit entry
│
├── vectorstore/ # Persistent vector data
├── scripts/ # Utility scripts
├── tests/ # Test suites
│ ├── backend/ # API tests
│ └── frontend/ # UI tests
│
├── .env.example # Environment template
├── .gitignore # Git ignore rules
├── LICENSE # MIT License
├── package.json # Node.js dependencies
├── requirements.txt # Python dependencies
└── README.md # This file

text

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
🏃 Running the Application
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

Reply rates (pattern matching)

Click-through rates

Response timing

Campaign performance

A/B test results

🤝 Contributing
We welcome contributions! Please follow these steps:

Fork the repository

Create a feature branch (git checkout -b feature/amazing-feature)

Commit your changes (git commit -m 'Add amazing feature')

Push to the branch (git push origin feature/amazing-feature)

Open a Pull Request

📜 License
Distributed under the MIT License. See LICENSE for more information.

📧 Contact
Project Maintainer - Your Name

Project Link: https://github.com/yourusername/voltmail

text

Key improvements made:

1. **Better Visual Organization**:
   - Added emojis for better visual scanning
   - Clearer section headers
   - Placeholder for banner image

2. **More Professional Structure**:
   - Separated features from tech stack
   - Added proper contact section
   - Clearer license information

3. **Corrected Folder Structure**:
   - Proper nesting for GitHub visibility
   - Added missing directories (tests, scripts)
   - Better naming conventions (components/, assets/)

4. **Enhanced Installation Guide**:
   - Prerequisites section
   - Step-by-step setup
   - Environment setup instructions

5. **Added Analytics Details**:
   - Specific metrics being tracked
   - Clear value proposition

6. **Standardized Contribution Guidelines**:
   - Conventional commits reference
   - Clear PR process

For GitHub, ensure:
1. Your actual repository matches this structure
2. Delete any unnecessary files/folders
3. Add a `.gitkeep` file in empty directories you want to preserve
4. Include a `.github` folder for issue templates, workflows etc. if needed

The structure now properly represents a production-ready application while maintaining developer clarity.
Screenshot 2025-07-18 233434.png
PNG 34.61KB
Screenshot 2025-07-18 233453.png
PNG 18.46KB
this is my folder structure now update my read me file
Here's an updated README.md that accurately reflects your current folder structure while maintaining professional organization:

markdown
# VoltMail: AI-Powered Cold Email Generator

![VoltMail Logo](https://via.placeholder.com/1200x400?text=VoltMail+Cold+Email+Generator) 
*(Replace with actual logo image)*

## ✨ Key Features
- **AI-Personalized Emails**: RAG-powered email generation
- **High Performance**: Groq + LLaMA3 integration
- **Context-Aware**: ChromaDB vector storage
- **Campaign Analytics**: Track email performance
- **Direct Sending**: Integrated email delivery

## 📂 Current Project Structure
voltmail/
├── .vscode/ # VS Code configurations
├── backend/ # Node.js backend
│ ├── controllers/
│ │ └── emailController.js # Email generation logic
│ ├── db/
│ │ ├── emaillog.js # MongoDB email logs
│ │ └── mongo.js # Database connection
│ ├── routes/
│ │ └── emailRoutes.js # API endpoints
│ ├── services/
│ │ ├── emailsender.js # Email delivery
│ │ ├── groqService.js # Groq LLM integration
│ │ └── promptBuilder.js # Prompt engineering
│ ├── .env # Backend environment
│ └── server.js # Express server
│
├── frontend/ # Streamlit interface
│ ├── pages/
│ │ ├── analytics.py # Metrics dashboard
│ │ ├── Home.py # Main interface
│ │ └── Voltmail.py # Email composer
│ ├── services/
│ │ ├── pycache/
│ │ └── langchain.py # RAG implementation
│ ├── utils/
│ │ ├── pycache/
│ │ ├── api_handler.py # Backend API calls
│ │ └── chroma_connector.py # Vector DB connection
│ └── groqproxy.py # Groq API helper
│
├── vectorstore/ # ChromaDB data
├── venv/ # Python virtual env
├── .env # Global environment
├── .gitignore # Git ignore rules
├── LICENSE # MIT License
├── package-lock.json # NPM dependencies
├── package.json # Node.js config
└── README.md # This file

text

## 🛠️ Setup Guide

### Prerequisites
- Node.js v16+
- Python 3.0+
- MongoDB Atlas or local instance
- Groq API key

1. **Clone repository**
   ```bash
   git clone https://github.com/yourusername/voltmail.git
   cd voltmail
Backend setup

bash
cd backend
npm install
cp .env.example .env  # Update with your credentials
Frontend setup

bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
Initialize services

bash
# Start MongoDB service first
cd ../backend
npm start
🚀 Running the Application
Backend (Port 5000)

bash
cd backend
npm start
Frontend (Port 8501)

bash
cd frontend
streamlit run Home.py
🔧 Key Components
File	Purpose
groqService.js	LLaMA3 integration
emailController.js	Core email generation
langchain.py	RAG implementation
chroma_connector.py	Vector DB management
analytics.py	Performance dashboard
📜 License
MIT License - See LICENSE for details.