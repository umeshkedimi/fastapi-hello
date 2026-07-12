# Contributing

Thanks for considering a contribution! This project aims to stay small and easy to fork, so please keep changes focused.

## Getting started

```bash
uv sync
uv run uvicorn main:app --reload
```

Run the app in Docker:

```bash
docker build -t fastapi-hello .
docker run -p 8000:8000 fastapi-hello
```

## Making a change

1. Fork the repo and create a branch from `main`.
2. Make your change, keeping it as small and focused as possible.
3. Make sure the app still runs locally and the Docker build succeeds.
4. Open a pull request describing what changed and why.

CI will build the Docker image and smoke-test the container on every pull request.

## Reporting issues

Open a GitHub issue with a clear description and, if possible, steps to reproduce.

## Code of conduct

This project follows the [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you're expected to uphold it.
