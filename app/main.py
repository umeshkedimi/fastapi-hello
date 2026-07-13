from fastapi import FastAPI

from app.api import chat, health
from app.logging import configure_logging

configure_logging()

app = FastAPI()
app.include_router(health.router)
app.include_router(chat.router)
