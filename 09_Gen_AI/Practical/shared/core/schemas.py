from pydantic import BaseModel, Field
from typing import Any


class HealthResponse(BaseModel):
    service: str
    status: str = "ok"


class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1)
    session_id: str | None = None
    provider: str | None = None
    model: str | None = None


class ChatResponse(BaseModel):
    answer: str
    provider: str
    model: str
    metadata: dict[str, Any] = Field(default_factory=dict)
