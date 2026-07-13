import logging

from fastapi import Depends, FastAPI
from pydantic import BaseModel

from app.logging import configure_logging
from app.providers import get_provider
from app.providers.base import ChatProvider

configure_logging()
logger = logging.getLogger("app")

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, world!"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


class ChatRequest(BaseModel):
    message: str
    provider: str | None = None


class ChatResponse(BaseModel):
    reply: str
    provider: str


def get_chat_provider() -> ChatProvider:
    return get_provider()


@app.post("/chat", response_model=ChatResponse)
async def chat(
    request: ChatRequest,
    provider: ChatProvider = Depends(get_chat_provider),
):
    if request.provider:
        provider = get_provider(request.provider)

    logger.info("chat request received", extra={"provider": provider.name})
    reply = await provider.complete(request.message)
    return ChatResponse(reply=reply, provider=provider.name)
