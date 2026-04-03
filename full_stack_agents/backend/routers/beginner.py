from fastapi import APIRouter

from schemas.models import BeginnerRequest, BeginnerResponse
from services import beginner_service

router = APIRouter(prefix="/api/beginner", tags=["beginner"])


@router.get("/examples")
async def get_examples() -> dict:
    examples = beginner_service.get_examples()
    return {"examples": [ex.model_dump() for ex in examples]}


@router.post("/analyze")
async def analyze_text(request: BeginnerRequest) -> BeginnerResponse:
    return await beginner_service.analyze_text(request.text, request.demo)
