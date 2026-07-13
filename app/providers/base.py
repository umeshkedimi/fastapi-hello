from abc import ABC, abstractmethod


class ChatProvider(ABC):
    name: str

    @abstractmethod
    async def complete(self, message: str) -> str:
        """Return a single completion for the given user message."""
