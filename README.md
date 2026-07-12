# fastapi-hello

[![Docker build](https://github.com/umeshkedimi/fastapi-hello/actions/workflows/docker-build.yml/badge.svg)](https://github.com/umeshkedimi/fastapi-hello/actions/workflows/docker-build.yml)

A minimal FastAPI service with a basic endpoint, managed with [uv](https://docs.astral.sh/uv/) and Docker.

## Run locally

```bash
uv sync
uv run uvicorn main:app --reload
```

Visit http://127.0.0.1:8000 or http://127.0.0.1:8000/health.

## Run with Docker

```bash
docker build -t fastapi-hello .
docker run -p 8000:8000 fastapi-hello
```
