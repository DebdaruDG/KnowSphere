from backend.services.vector_store import get_vector_store
from backend.utils.file_reader import read_pdf

def embed_and_store(file_path: str):
    documents = read_pdf(file_path)
    vectordb = get_vector_store()
    vectordb.add_documents(documents)
    vectordb.persist()
