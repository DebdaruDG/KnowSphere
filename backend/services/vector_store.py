from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings

persist_dir = "vector_store"
embedding = OpenAIEmbeddings()

def get_vector_store():
    return Chroma(persist_directory=persist_dir, embedding_function=embedding)