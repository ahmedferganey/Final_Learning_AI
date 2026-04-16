from dataclasses import dataclass


@dataclass
class RetrievedChunk:
    text: str
    score: float
    source: str
