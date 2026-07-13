# Contributing

Thanks for considering a contribution! This project aims to stay small and easy to fork, so please keep changes focused.

## Getting started

```bash
uv sync
uv run pre-commit install
uv run uvicorn main:app --reload
```

`pre-commit install` sets up a git hook that runs ruff and pytest automatically
before each commit, so issues get caught locally instead of in CI.

Run the app in Docker:

```bash
docker build -t agentic-fastapi-template .
docker run -p 8000:8000 agentic-fastapi-template
```

## Making a change

1. Fork the repo and create a branch from `main`.
2. Make your change, keeping it as small and focused as possible.
3. Commit — the pre-commit hook runs ruff and pytest automatically. You can
   also run them manually with `uv run ruff check .`, `uv run ruff format .`,
   and `uv run pytest`.
4. Make sure the Docker build succeeds.
5. Open a pull request describing what changed and why.

CI will lint, run tests, then build the Docker image and smoke-test the container on every pull request.

## Reporting issues

Open a GitHub issue with a clear description and, if possible, steps to reproduce.

## Code of conduct

This project follows the [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you're expected to uphold it.
