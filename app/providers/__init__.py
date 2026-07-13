from functools import lru_cache

from app.config import get_settings
from app.providers.anthropic_provider import AnthropicProvider
from app.providers.base import ChatProvider
from app.providers.openai_provider import OpenAIProvider


@lru_cache
def get_provider(name: str | None = None) -> ChatProvider:
    settings = get_settings()
    provider_name = name or settings.default_provider

    if provider_name == "anthropic":
        return AnthropicProvider(
            api_key=settings.anthropic_api_key, model=settings.anthropic_model
        )
    if provider_name == "openai":
        return OpenAIProvider(
            api_key=settings.openai_api_key, model=settings.openai_model
        )

    raise ValueError(f"Unknown provider: {provider_name}")


def get_chat_provider() -> ChatProvider:
    return get_provider()
