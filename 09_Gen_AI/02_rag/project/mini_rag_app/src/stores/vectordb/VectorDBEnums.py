from enum import Enum

class VectorDBEnums(Enum):
    QDRANT = "QDRANT"
    PGVECTOR = "PGVECTOR"

class DistanceMethodEnums(Enum):
    COSINE = "cosine"
    EUCLIDEAN = "euclidean"
    MANHATTAN = "manhattan"
    Dot = "dot"


class PGVectorIndexTypeEnums(Enum):
    HNSW = "hnsw"
    IVFFLAT = "ivfflat"
    NONE = "none"


class PGVectorDistanceMethodEnums(Enum):
    COSINE = "cosine"
    L2 = "l2"
    IP = "ip"
