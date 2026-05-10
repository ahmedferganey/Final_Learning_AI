from pydantic import BaseModel
from typing import Optional


class PushRequest(BaseModel):
    do_reset: Optional[int] = 0
    # You can add more fields here if needed, e.g., data to be indexed, metadata, etc.


class SearchRequest(BaseModel):
    query_text: str
    top_k: Optional[int] = 5
    limit: Optional[int] = 5


class RagAnswerRequest(BaseModel):
    question: str
    language: Optional[str] = None
    top_k: Optional[int] = 5
    limit: Optional[int] = 5
    temperature: Optional[float] = None
    max_output_tokens: Optional[int] = None
    system_message: Optional[str] = None
    debug: Optional[bool] = False
    include_chat_history: Optional[bool] = False
