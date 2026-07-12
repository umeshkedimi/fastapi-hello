# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Basic FastAPI app with `/` and `/health` endpoints, managed with `uv`.
- `Dockerfile` and `.dockerignore` to containerize the app.
- GitHub Actions CI: builds the Docker image and smoke-tests the container.
- CI status badge in the README.
- MIT license.
- `CONTRIBUTING.md` and a Contributor Covenant `CODE_OF_CONDUCT.md`.
- Marked the repo as a GitHub template.
- `pytest` tests for both endpoints, wired into CI.
- `ruff` for linting and formatting, wired into CI.
- `pre-commit` hook running ruff and pytest before each commit.
