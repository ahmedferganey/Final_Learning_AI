from fastapi import FastAPI
from shared.core.schemas import HealthResponse

app = FastAPI(title="chat_service")


@app.get("/health", response_model=HealthResponse)
async def health() -> HealthResponse:
    return HealthResponse(service="chat_service")


from shared.core.schemas import ChatRequest, ChatResponse
from shared.llm.providers import MockLLMClient

client = MockLLMClient()


@app.post("/chat", response_model=ChatResponse)
async def chat(payload: ChatRequest) -> ChatResponse:
    answer = await client.generate(payload.message)
    return ChatResponse(
        answer=answer,
        provider=payload.provider or "mock",
        model=payload.model or "mock-model",
        metadata={"session_id": payload.session_id},
    )
