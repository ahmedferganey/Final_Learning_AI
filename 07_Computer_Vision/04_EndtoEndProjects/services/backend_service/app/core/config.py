from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    FIREBASE_PROJECT_ID: str = ""

    class Config:
        env_file = ".env"

settings = Settings()
