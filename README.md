# agentic-fastapi-template

[![Docker build](https://github.com/umeshkedimi/agentic-fastapi-template/actions/workflows/docker-build.yml/badge.svg)](https://github.com/umeshkedimi/agentic-fastapi-template/actions/workflows/docker-build.yml)

A minimal, fork-friendly FastAPI starter for building agentic AI apps — managed with [uv](https://docs.astral.sh/uv/) and Docker, with a pluggable LLM provider layer (OpenAI + Anthropic).

## Run locally

```bash
uv sync
cp .env.example .env  # then fill in an API key for at least one provider
uv run uvicorn app.main:app --reload
```

Visit http://127.0.0.1:8000 or http://127.0.0.1:8000/health.

## Chat endpoint

```bash
curl -X POST http://127.0.0.1:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "hello"}'
```

`provider` is optional in the request body (`"openai"` or `"anthropic"`) and overrides `DEFAULT_PROVIDER` from `.env` for that request. Providers live in `app/providers/` behind a small `ChatProvider` interface — add a new one by implementing `complete()` and registering it in `app/providers/__init__.py`.

## Project layout

```
app/
├── main.py         # FastAPI app instance, includes routers
├── api/            # route handlers (health.py, chat.py, ...)
├── schemas/        # Pydantic request/response models
├── providers/       # ChatProvider interface + OpenAI/Anthropic implementations
├── config.py        # pydantic-settings config
└── logging.py        # structured JSON logging setup
tests/
```

## Run with Docker

```bash
docker build -t agentic-fastapi-template .
docker run -p 8000:8000 agentic-fastapi-template
```
