from fastapi import FastAPI
from shared.core.schemas import HealthResponse

app = FastAPI(title="gateway_api")


@app.get("/health", response_model=HealthResponse)
async def health() -> HealthResponse:
    return HealthResponse(service="gateway_api")


from fastapi import APIRouter

router = APIRouter(prefix="/v1")

@router.get("/routes")
async def list_routes() -> dict:
    return {
        "services": {
            "chat": "http://localhost:8001/chat",
            "rag_ingest": "http://localhost:8002/ingest",
            "rag_query": "http://localhost:8002/query",
            "agent_run": "http://localhost:8003/run",
            "eval": "http://localhost:8004/evaluate",
        }
    }

app.include_router(router)
