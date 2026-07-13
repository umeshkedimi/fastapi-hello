from fastapi.testclient import TestClient

from app.providers.base import ChatProvider
from main import app, get_chat_provider


class FakeProvider(ChatProvider):
    name = "fake"

    async def complete(self, message: str) -> str:
        return f"echo: {message}"


app.dependency_overrides[get_chat_provider] = lambda: FakeProvider()
client = TestClient(app)


def test_chat_returns_reply_from_provider():
    response = client.post("/chat", json={"message": "hello"})
    assert response.status_code == 200
    assert response.json() == {"reply": "echo: hello", "provider": "fake"}
