from functools import lru_cache
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    default_provider: Literal["openai", "anthropic"] = "anthropic"

    anthropic_api_key: str | None = None
    anthropic_model: str = "claude-opus-4-8"

    openai_api_key: str | None = None
    openai_model: str = "gpt-4o-mini"


@lru_cache
def get_settings() -> Settings:
    return Settings()
