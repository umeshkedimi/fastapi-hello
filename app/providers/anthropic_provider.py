from anthropic import AsyncAnthropic

from app.providers.base import ChatProvider


class AnthropicProvider(ChatProvider):
    name = "anthropic"

    def __init__(self, api_key: str | None, model: str) -> None:
        self._client = AsyncAnthropic(api_key=api_key)
        self._model = model

    async def complete(self, message: str) -> str:
        response = await self._client.messages.create(
            model=self._model,
            max_tokens=1024,
            messages=[{"role": "user", "content": message}],
        )
        return next(
            (block.text for block in response.content if block.type == "text"), ""
        )
