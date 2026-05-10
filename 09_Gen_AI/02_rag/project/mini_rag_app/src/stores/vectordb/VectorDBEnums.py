from enum import Enum

class VectorDBEnums(Enum):
    PINECONE = "PINECONE"
    VERTEX_AI = "VERTEX_AI"
    QDRANT = "QDRANT"

class DistanceMethodEnums(Enum):
    COSINE = "cosine"
    EUCLIDEAN = "euclidean"
    MANHATTAN = "manhattan"
    Dot = "dot"

