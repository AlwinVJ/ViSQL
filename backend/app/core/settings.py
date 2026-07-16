from functools import lru_cache

from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "ViSQL API"
    app_version: str = "0.1.0"
    api_v1_prefix: str = "/api/v1"
    database_url: str = "postgresql+psycopg://visql:change-me-in-production@localhost:5432/visql"
    openai_api_key: str = ""
    openai_model: str = "gpt-4.1-mini"
    log_level: str = "INFO"
    cors_origins: list[str] = ["http://localhost:3000"]

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    @field_validator("cors_origins", mode="before")
    @classmethod
    def parse_cors_origins(cls, value: str | list[str]) -> list[str]:
        return [origin.strip() for origin in value.split(",") if origin.strip()] if isinstance(value, str) else value


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()

