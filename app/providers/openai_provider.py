from openai import AsyncOpenAI

from app.providers.base import ChatProvider


class OpenAIProvider(ChatProvider):
    name = "openai"

    def __init__(self, api_key: str | None, model: str) -> None:
        self._client = AsyncOpenAI(api_key=api_key)
        self._model = model

    async def complete(self, message: str) -> str:
        response = await self._client.chat.completions.create(
            model=self._model,
            messages=[{"role": "user", "content": message}],
        )
        return response.choices[0].message.content or ""
