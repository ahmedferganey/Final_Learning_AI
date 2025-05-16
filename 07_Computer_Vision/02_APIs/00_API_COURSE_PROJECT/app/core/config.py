from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    PROJECT_NAME: str = "My_API_Project"
    class Config:
        env_file = ".env"

settings = Settings()
