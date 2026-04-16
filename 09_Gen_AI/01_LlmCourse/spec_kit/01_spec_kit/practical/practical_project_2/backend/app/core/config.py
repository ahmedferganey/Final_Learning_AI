from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    app_env: str
    app_version: str = "0.1.0"
    port: int = 8000

    database_url: str
    redis_url: str


def get_settings() -> Settings:
    return Settings()  # type: ignore[call-arg]
