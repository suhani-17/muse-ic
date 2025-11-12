from fastapi import APIRouter, Depends
from pydantic import BaseModel

router = APIRouter()

class MoodRequest(BaseModel):
    mood_text: str
    top_k: int = 10

@router.post("/recommend")
async def recommend(req: MoodRequest):
    # 1) normalize -> matched_tags OR embedding
    # 2) query DB -> candidates
    # 3) score and return
    return {"results": []}
