import os
from dotenv import load_dotenv
from langchain_cohere import CohereEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))
cohere_api_key = os.getenv("COHERE_API_KEY")
persist_dir = os.path.join(os.path.dirname(__file__), '..', 'vectorstore')
embedding_model = CohereEmbeddings(cohere_api_key=cohere_api_key)
def get_vectorstore():
    return Chroma(
        persist_directory=persist_dir,
        embedding_function=embedding_model
    )
def add_text_to_chroma(text: str, metadata: dict = None):
    if not metadata:
        metadata = {}
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )
    chunks = splitter.create_documents([text], metadatas=[metadata])
    vectordb = get_vectorstore()
    vectordb.add_documents(chunks)
    vectordb.persist()
    return len(chunks)
