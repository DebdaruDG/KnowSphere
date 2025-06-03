from fastapi import APIRouter, UploadFile, File, HTTPException
from backend.services.embedder import embed_and_store
import os, uuid, shutil

router = APIRouter()

@router.post("/")
async def upload_file(file: UploadFile = File(...)):
    try:
        file_id = str(uuid.uuid4())
        os.makedirs("temp_docs", exist_ok=True)
        file_path = f"temp_docs/{file_id}_{file.filename}"
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        embed_and_store(file_path)
        os.remove(file_path)
        return {"message": "File uploaded and embedded", "doc_id": file_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))