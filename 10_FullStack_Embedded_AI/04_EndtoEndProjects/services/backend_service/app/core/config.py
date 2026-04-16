from pydantic_settings import BaseSettings
from functools import lru_cache



class Settings(BaseSettings):
    PROJECT_NAME: str = "Backend Service"
    VERSION: str = "1.0.0"
    RABBITMQ_HOST: str = "rabbitmq"
    RABBITMQ_USER: str = "guest"
    RABBITMQ_PASS: str = "guest"
    RABBITMQ_PORT: int = 5672
    rabbitmq_queue: str = "frame_queue"
    postgres_user: str
    postgres_password: str
    postgres_db: str
    postgres_host: str = "postgres"

    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()

settings = get_settings()
