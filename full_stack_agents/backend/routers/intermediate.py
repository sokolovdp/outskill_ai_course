import json

from fastapi import APIRouter
from sse_starlette.sse import EventSourceResponse

from schemas.models import IntermediateRequest
from services import intermediate_service

router = APIRouter(prefix="/api/intermediate", tags=["intermediate"])


@router.get("/logs")
async def get_logs() -> dict:
    logs = intermediate_service.get_log_files()
    return {"logs": [log.model_dump() for log in logs]}


@router.post("/analyze")
async def analyze_logs(request: IntermediateRequest) -> EventSourceResponse:
    async def event_generator():
        async for event in intermediate_service.analyze_logs_stream(request.log_file, request.demo):
            yield {"data": json.dumps(event)}

    return EventSourceResponse(event_generator())
