from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from backend.services.vector_store import get_vector_store

def get_answer(query: str) -> str:
    vectordb = get_vector_store()
    retriever = vectordb.as_retriever(search_kwargs={"k": 3})
    qa_chain = RetrievalQA.from_chain_type(llm=ChatOpenAI(), chain_type="stuff", retriever=retriever)
    return qa_chain.run(query)