Cold Email Generator with RAG & Analytics
This project is an advanced Cold Email Generator designed to create highly personalized cold emails using Retrieval-Augmented Generation (RAG), powered by large language models and a robust analytics dashboard. It leverages a modern tech stack including Groq (LLaMA3) for fast inference, ChromaDB for vector storage, Cohere for embeddings, MongoDB for data persistence, and a Streamlit frontend for an intuitive user experience.

Features
Personalized Email Generation: Utilizes Retrieval-Augmented Generation (RAG) with ChromaDB to fetch relevant context and generate highly personalized cold emails.

Groq (LLaMA3) Integration: Employs Groq for rapid and efficient email generation, leveraging the power of LLaMA3.

Cohere Embeddings: Uses Cohere's powerful embedding models for creating vector representations of data, crucial for effective RAG.

MongoDB for Data Storage: Persists email logs, analytics data, and other relevant information in a MongoDB database.

Express.js Backend: A robust Node.js backend handles API requests, interacts with the database, and orchestrates email sending and LLM calls.

Streamlit Frontend: Provides an interactive and user-friendly interface for generating emails, managing campaigns, and viewing analytics.

Email Sending Functionality: Integrates with email APIs (e.g., Gmail API or SendGrid) to send generated emails directly from the application.

Analytics Dashboard: A dedicated Streamlit dashboard to track key metrics such as email opens, replies, and other engagement data, providing insights into campaign performance.

Folder Structure
The project is organized into backend, frontend, and utility directories for clear separation of concerns:

.
├── .vscode/               # VS Code specific settings
├── backend/               # Express.js server for API, DB, and LLM orchestration
│   ├── controllers/
│   │   └── emailController.js  # Business logic for email operations
│   ├── db/
│   │   ├── emaillog.js         # MongoDB schema for email logs
│   │   └── mongo.js            # MongoDB connection setup
│   ├── routes/
│   │   └── emailRoutes.js      # API routes for email generation and management
│   ├── services/
│   │   ├── emailsender.js      # Logic for sending emails (e.g., Gmail API, SendGrid)
│   │   ├── groqService.js      # Integration with Groq API for LLM inference
│   │   └── promptBuilder.js    # Utility to construct prompts for LLMs
│   ├── .env                    # Environment variables for the backend
│   └── server.js               # Main entry point for the Express.js server
├── frontend/              # Streamlit application for the user interface
│   ├── pages/
│   │   ├── analytics.py        # Streamlit page for the analytics dashboard
│   │   ├── Home.py             # Main Streamlit page for email generation
│   │   └── Voltmail.py         # Another main page or specific feature page
│   ├── services/
│   │   └── langchain.py        # LangChain integration for RAG logic within Streamlit
│   └── utils/
│       ├── api_handler.py      # Handles API calls from frontend to backend
│       ├── chroma_connector.py # Connects to ChromaDB for vector operations
│       └── groqproxy.py        # Proxy or direct integration for Groq from frontend (if applicable)
├── vectorstore/           # Directory to store ChromaDB persistent data
├── .env                   # Global environment variables
├── app.py                 # Main Streamlit application entry point
├── node_modules/          # Node.js dependencies
├── venv/                  # Python virtual environment
├── .gitignore             # Git ignore file
├── package-lock.json      # Node.js dependency lock file
├── package.json           # Node.js project metadata and dependencies
└── README.md              # This README file

Technologies Used
Backend: Node.js, Express.js

Frontend: Streamlit, Python

Database: MongoDB

Vector Database: ChromaDB

LLM Inference: Groq (LLaMA3)

Embeddings: Cohere

Email Service: Gmail API / SendGrid (or similar)

Orchestration: LangChain (for RAG)

Setup and Installation
Follow these steps to set up and run the project locally.

Prerequisites
Node.js (LTS version recommended)

Python 3.0+

MongoDB (local installation or cloud-hosted instance)

Git

1. Clone the Repository
git clone <your-repository-url>
cd cold-email-generator

2. Environment Variables Setup
Create a .env file in the root directory and another .env file inside the backend/ directory. Populate them with your API keys and database connection strings:

Root .env (for Streamlit):

COHERE_API_KEY="your_cohere_api_key"
GROQ_API_KEY="your_groq_api_key"
# Add any other frontend-specific environment variables here

backend/.env (for Express.js):

PORT=5000
MONGO_URI="your_mongodb_connection_string" # e.g., mongodb://localhost:27017/cold_email_db
GMAIL_API_CLIENT_ID="your_gmail_client_id"
GMAIL_API_CLIENT_SECRET="your_gmail_client_secret"
GMAIL_API_REDIRECT_URI="http://localhost:5000/auth/gmail/callback" # Or your deployed redirect URI
# Or if using SendGrid:
# SENDGRID_API_KEY="your_sendgrid_api_key"
GROQ_API_KEY="your_groq_api_key" # Duplicate for backend usage if needed
COHERE_API_KEY="your_cohere_api_key" # Duplicate for backend usage if needed

3. Backend Setup
Navigate to the backend directory and install dependencies:

cd backend
npm install

4. Frontend Setup
Navigate back to the root directory, create a Python virtual environment, and install dependencies:

cd .. # If you are still in the backend directory
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

Note: You will need to create a requirements.txt file in the root directory that lists all Python dependencies, e.g.:

streamlit
pymongo
langchain
chromadb
cohere
groq
python-dotenv

Running the Application
1. Start the MongoDB Server
Ensure your MongoDB instance is running. If you're using a local MongoDB, start it.

2. Start the Backend Server
Open a new terminal, navigate to the backend directory, and start the Express.js server:

cd backend
npm start

The backend server will typically run on http://localhost:5000 (or the port specified in your .env).

3. Start the Streamlit Frontend
Open another new terminal, navigate to the root directory, activate your Python virtual environment, and run the Streamlit application:

source venv/bin/activate # On Windows: venv\Scripts\activate
streamlit run app.py

This will open the Streamlit application in your web browser, usually at http://localhost:8501.

Usage
Once both the backend and frontend are running:

Navigate to the Home page (Home.py) in the Streamlit app to generate cold emails.

Provide necessary inputs (e.g., recipient information, context for personalization).

The application will use RAG with ChromaDB and Groq to generate a personalized email.

You can then send the email through the integrated email sending functionality.

Visit the Analytics page (analytics.py) to view the performance of your sent emails, including opens and replies.

Contributing
Contributions are welcome! Please follow these steps:

Fork the repository.

Create a new branch (git checkout -b feature/your-feature-name).

Make your changes.

Commit your changes (git commit -m 'Add new feature').

Push to the branch (git push origin feature/your-feature-name).

Open a Pull Request.

