from pydantic import BaseModel

class UploadResponse(BaseModel):
    message: str
    doc_id: str

class AskRequest(BaseModel):
    question: str

class AskResponse(BaseModel):
    answer: str