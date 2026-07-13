import logging

from fastapi import APIRouter, Depends

from app.providers import get_chat_provider, get_provider
from app.providers.base import ChatProvider
from app.schemas.chat import ChatRequest, ChatResponse

logger = logging.getLogger("app")

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
async def chat(
    request: ChatRequest,
    provider: ChatProvider = Depends(get_chat_provider),
):
    if request.provider:
        provider = get_provider(request.provider)

    logger.info("chat request received", extra={"provider": provider.name})
    reply = await provider.complete(request.message)
    return ChatResponse(reply=reply, provider=provider.name)
