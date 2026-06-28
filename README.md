# Stock LLM Lab

## Project Overview

Stock LLM Lab is a long-term learning and research repository. The project has two goals:

1. Learn how LLMs work by building a tiny GPT-style model from scratch.
2. Use that foundation to build a practical stock research system with retrieval, tools, specialist agents, and backtesting.

This repository is intentionally starting with a clean engineering foundation before any model training or finance logic is implemented.

## Current Status

The project is in the repository foundation stage. The current focus is:

- Python package structure
- Basic test and quality tooling
- Repository conventions
- Documentation and workflow guardrails

No tokenizer, training loop, agent system, retrieval pipeline, or financial analysis engine has been implemented yet.

## High-Level Roadmap

1. Establish repo structure, quality checks, and documentation.
2. Add a small dataset/tokenizer pipeline for the educational tiny-LLM track.
3. Implement a minimal decoder-only transformer and training loop.
4. Build evaluation and experiment-tracking foundations.
5. Add retrieval, finance tooling, agent orchestration, and backtesting in later milestones.

## Setup

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e .[dev]
```

## Development Workflow

```powershell
python -m pytest
python -m ruff format . --no-cache
python -m ruff check . --no-cache
```

Suggested workflow:

1. Create a small feature branch.
2. Make a focused change.
3. Run tests and quality checks.
4. Update documentation if behavior or workflow changed.
5. Update `PROJECT_CONTEXT.md` before ending the session.

## Safety And Legal Disclaimer

This is research software for learning and experimentation. It is not financial advice, not an investment recommendation system, and not a regulated advisory product. Any future outputs should be treated as research artifacts and reviewed critically by a human.
