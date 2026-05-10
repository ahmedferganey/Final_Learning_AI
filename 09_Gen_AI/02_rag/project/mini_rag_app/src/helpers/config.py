from pydantic_settings import BaseSettings
from urllib.parse import quote_plus

class Settings(BaseSettings):

    APP_NAME: str
    APP_VERSION: str
    OPENAI_API_KEY: str

    FILE_ALLOWED_TYPES: list
    FILE_MAX_SIZE: int
    FILE_DEFAULT_CHUNK_SIZE: int

    MONGODB_URL: str
    MONGODB_DATABASE: str
    MONGODB_USERNAME: str = ""
    MONGODB_PASSWORD: str = ""
    MONGODB_HOST: str = ""
    MONGODB_PORT: int = 27017
    MONGODB_AUTH_SOURCE: str = "admin"

    GENERATION_BACKEND: str
    EMBEDDING_BACKEND: str

    OPENAI_API_KEY: str = None
    OPENAI_API_URL: str = None
    COHERE_API_KEY: str = None

    GENERATION_MODEL_ID: str = None
    EMBEDDING_MODEL_ID: str = None
    EMBEDDING_MODEL_SIZE: int = None
    INPUT_DAFAULT_MAX_CHARACTERS: int = None
    GENERATION_DAFAULT_MAX_TOKENS: int = None
    GENERATION_DAFAULT_TEMPERATURE: float = None

    VECTOR_DB_BACKEND: str
    VECTOR_DB_PATH: str
    VECTOR_DB_DISTANCE_METHOD: str = None


    class Config:
        env_file = ".env"

    def get_mongodb_url(self):
        if self.MONGODB_URL:
            return self.MONGODB_URL

        if self.MONGODB_USERNAME and self.MONGODB_PASSWORD and self.MONGODB_HOST:
            username = quote_plus(self.MONGODB_USERNAME)
            password = quote_plus(self.MONGODB_PASSWORD)
            return (
                f"mongodb://{username}:{password}@{self.MONGODB_HOST}:{self.MONGODB_PORT}"
                f"/?authSource={self.MONGODB_AUTH_SOURCE}"
            )

        return ""

def get_settings():
    return Settings()
