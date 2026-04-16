from pydantic_settings import BaseSettings
from pathlib import Path
import os

ENV = os.getenv("ENV", "development")
RUNNING_IN_DOCKER = os.getenv("RUNNING_IN_DOCKER") == "1"

env_file_map = {
    "development": Path(__file__).resolve().parents[2] / ".env.dev",
    "production": Path(__file__).resolve().parents[2] / ".env.prod",
}

class AppSettings(BaseSettings):
    PROJECT_NAME: str = "Backend Gateway"
    ENV: str = ENV
    DEBUG: bool = True
    DATABASE_URL: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str = "5432"
    POSTGRES_DB: str

    RABBITMQ_URL: str
    FIREBASE_PROJECT_ID: str
    FIREBASE_CREDENTIALS: str

    @property
    def SQLALCHEMY_DATABASE_URI(self) -> str:
        return (
            f"postgresql+psycopg2://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )

    class Config:
        env_file = None if RUNNING_IN_DOCKER else str(env_file_map.get(ENV))
        case_sensitive = True

settings = AppSettings()

print(f"[config] Loaded settings from: {AppSettings.Config.env_file}")
print(f"[config] Loaded environment: {settings.ENV}")
print(f"[config] DB URL: {settings.SQLALCHEMY_DATABASE_URI}")
print(f"[config] DEBUG mode: {settings.DEBUG}")
