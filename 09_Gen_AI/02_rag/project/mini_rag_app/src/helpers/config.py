from pydantic_settings import BaseSettings
from urllib.parse import quote_plus
from typing import List

class Settings(BaseSettings):

    APP_NAME: str
    APP_VERSION: str

    FILE_ALLOWED_TYPES: list
    FILE_MAX_SIZE: int
    FILE_DEFAULT_CHUNK_SIZE: int

    DATABASE_URL: str = ""
    POSTGRES_USERNAME: str = ""
    POSTGRES_USER: str = ""
    POSTGRES_PASSWORD: str = ""
    POSTGRES_PORT: int = 5432
    POSTGRES_HOST: str = ""
    POSTGRES_MAIN_DATABASE: str = ""
    POSTGRES_DB: str = ""

    GENERATION_BACKEND: str
    EMBEDDING_BACKEND: str

    OPENAI_API_KEY: str = None
    OPENAI_API_URL: str = None
    COHERE_API_KEY: str = None

    GENERATION_MODEL_ID_LITERAL: List[str] = None
    GENERATION_MODEL_ID: str = None
    EMBEDDING_MODEL_ID: str = None
    EMBEDDING_MODEL_SIZE: int = None
    INPUT_DAFAULT_MAX_CHARACTERS: int = None
    GENERATION_DAFAULT_MAX_TOKENS: int = None
    GENERATION_DAFAULT_TEMPERATURE: float = None

    VECTOR_DB_BACKEND_LITERAL: List[str] = None
    VECTOR_DB_BACKEND: str
    VECTOR_DB_PATH: str = "qdrant_db"
    VECTOR_DB_DISTANCE_METHOD: str = None

    # PGVector config (used when VECTOR_DB_BACKEND="PGVECTOR")
    PGVECTOR_INDEX_TYPE: str = "hnsw"
    PGVECTOR_DISTANCE_METHOD: str = "cosine"

    # Templates / localization
    DEFAULT_LANGUAGE: str = "en"

    class Config:
        env_file = ".env"

    def get_database_url(self) -> str:
        if self.DATABASE_URL:
            return self.DATABASE_URL

        username = self.POSTGRES_USERNAME or self.POSTGRES_USER
        db_name = self.POSTGRES_MAIN_DATABASE or self.POSTGRES_DB

        if username and self.POSTGRES_PASSWORD and self.POSTGRES_HOST and db_name:
            encoded_user = quote_plus(username)
            encoded_pass = quote_plus(self.POSTGRES_PASSWORD)
            return (
                f"postgresql+asyncpg://{encoded_user}:{encoded_pass}"
                f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{db_name}"
            )

        raise ValueError(
            "Database configuration is missing. Set DATABASE_URL or POSTGRES credentials."
        )


def get_settings():
    return Settings()
