import os
from pinecone import Pinecone, ServerlessSpec
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore

class VectorStore:
    def __init__(self, index_name="ai-knowledge-base"):
        self.pinecone_client = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
        self.index_name = index_name
        self.embeddings = OpenAIEmbeddings(model="text-embedding-3-small", openai_api_key=os.getenv("OPENAI_API_KEY"))

        # Check if index exists, create if not
        if self.index_name not in self.pinecone_client.list_indexes().names():
            self.pinecone_client.create_index(
                name=self.index_name,
                dimension=1536,
                metric="dotproduct",
                spec=ServerlessSpec(cloud="aws", region="us-east-1")
            )

    def get_vector_store(self):
        return PineconeVectorStore(
            index_name=self.index_name,
            embedding=self.embeddings,
            pinecone_api_key=os.getenv("PINECONE_API_KEY")
        )