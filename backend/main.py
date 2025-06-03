# main.py
from fastapi import FastAPI
from backend.routes import upload, ask

app = FastAPI()

app.include_router(upload.router, prefix="/upload", tags=["Upload"])
app.include_router(ask.router, prefix="/ask", tags=["Ask"])

@app.get("/")
def root():
    return {"message": "AI Knowledge Base Backend"}
