from fastapi import FastAPI
from shared.core.schemas import HealthResponse

app = FastAPI(title="agent_service")


@app.get("/health", response_model=HealthResponse)
async def health() -> HealthResponse:
    return HealthResponse(service="agent_service")


from pydantic import BaseModel

class AgentRequest(BaseModel):
    goal: str
    tools: list[str] = []

@app.post("/run")
async def run_agent(payload: AgentRequest) -> dict:
    return {
        "goal": payload.goal,
        "selected_tools": payload.tools,
        "steps": [
            {"step": 1, "action": "analyze_goal"},
            {"step": 2, "action": "select_tools"},
            {"step": 3, "action": "produce_result"},
        ],
        "result": "Stub agent result",
    }
