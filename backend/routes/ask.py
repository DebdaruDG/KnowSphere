from fastapi import APIRouter, HTTPException
from backend.models.schemas import AskRequest, AskResponse
from backend.services.qa import get_answer

router = APIRouter()

@router.post("/", response_model=AskResponse)
async def ask_question(payload: AskRequest):
    try:
        answer = get_answer(payload.question)
        return AskResponse(answer=answer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))