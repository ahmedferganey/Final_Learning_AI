from fastapi import FastAPI
from shared.core.schemas import HealthResponse

app = FastAPI(title="rag_service")


@app.get("/health", response_model=HealthResponse)
async def health() -> HealthResponse:
    return HealthResponse(service="rag_service")


from pydantic import BaseModel
from shared.rag.chunking import simple_chunk_text

class IngestRequest(BaseModel):
    source_name: str
    text: str

class QueryRequest(BaseModel):
    question: str
    context: str

@app.post("/ingest")
async def ingest(payload: IngestRequest) -> dict:
    chunks = simple_chunk_text(payload.text)
    return {"source_name": payload.source_name, "chunks_created": len(chunks)}

@app.post("/query")
async def query(payload: QueryRequest) -> dict:
    return {
        "question": payload.question,
        "answer": "Stub grounded answer",
        "citations": [{"source": "inline_context", "score": 1.0}],
    }
