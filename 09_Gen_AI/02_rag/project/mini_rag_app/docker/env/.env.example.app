OPENAI_API_KEY=""

APP_NAME="mini-RAG"
APP_VERSION="0.1"


FILE_ALLOWED_TYPES=["text/plain", "application/pdf"]
FILE_MAX_SIZE=10
FILE_DEFAULT_CHUNK_SIZE=512000

# Database Initialization
POSTGRES_USERNAME="postgres"
POSTGRES_PASSWORD="postgres_password"

# Connection helper for your app/DBeaver
POSTGRES_PORT=5432
POSTGRES_HOST="pgvector"

# perhabs we will have other databases not the main only
POSTGRES_MAIN_DATABASE="minirag"


# ============ LLM Config ===========
GENERATION_BACKEND="COHERE"
EMBEDDING_BACKEND="COHERE"

OPENAI_API_KEY=""
OPENAI_API_URL=""
COHERE_API_KEY=""

GENERATION_MODEL_ID_LITERAL=["command-r7b-12-2024","gpt-4o-mini"]
GENERATION_MODEL_ID="command-r7b-12-2024"
EMBEDDING_MODEL_ID="embed-multilingual-light-v3.0"
EMBEDDING_MODEL_SIZE=384

INPUT_DAFAULT_MAX_CHARACTERS=1024
GENERATION_DAFAULT_MAX_TOKENS=200
GENERATION_DAFAULT_TEMPERATURE=0.1

#=========== VectorDB Config ===========
VECTOR_DB_BACKEND_LITERAL=["PGVECTOR","QDRANT"]
VECTOR_DB_BACKEND="PGVECTOR"
VECTOR_DB_PATH="qdrant_db"
VECTOR_DB_DISTANCE_METHOD="cosine"

# ============ Templates / Localization ===========
DEFAULT_LANGUAGE="en"


