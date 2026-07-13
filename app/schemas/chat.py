from pydantic import BaseModel


class ChatRequest(BaseModel):
    message: str
    provider: str | None = None


class ChatResponse(BaseModel):
    reply: str
    provider: str
