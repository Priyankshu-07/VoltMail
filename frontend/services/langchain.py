from utils.chroma_connector import get_vectorstore
def get_context_from_rag(query: str, top_k: int = 3) -> str:
    vectordb = get_vectorstore()
    results = vectordb.similarity_search(query, k=top_k)
    context = "\n---\n".join([doc.page_content for doc in results])
    return context
