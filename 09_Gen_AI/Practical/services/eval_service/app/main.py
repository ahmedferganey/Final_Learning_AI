from fastapi import FastAPI
from shared.core.schemas import HealthResponse

app = FastAPI(title="eval_service")


@app.get("/health", response_model=HealthResponse)
async def health() -> HealthResponse:
    return HealthResponse(service="eval_service")


from pydantic import BaseModel

class EvalRequest(BaseModel):
    task_name: str
    predictions: list[str]
    references: list[str]

@app.post("/evaluate")
async def evaluate(payload: EvalRequest) -> dict:
    total = min(len(payload.predictions), len(payload.references))
    exact = sum(1 for p, r in zip(payload.predictions, payload.references) if p == r)
    accuracy = (exact / total) if total else 0.0
    return {
        "task_name": payload.task_name,
        "samples": total,
        "exact_match": accuracy,
    }
