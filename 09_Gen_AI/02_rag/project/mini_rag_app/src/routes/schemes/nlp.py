from pydantic import BaseModel
from typing import Optional


class PushRequest(BaseModel):
    do_reset: Optional[int] = 0
    # You can add more fields here if needed, e.g., data to be indexed, metadata, etc.


class SearchRequest(BaseModel):
    query_text: str
    top_k: Optional[int] = 5
    limit: Optional[int] = 5
