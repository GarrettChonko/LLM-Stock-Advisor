# AGENTS.md

## Project Purpose

Stock LLM Lab is a long-term learning and research project with two tracks:

- Build a tiny GPT-style model from scratch to learn core LLM internals.
- Build a practical stock research system using open-source models, retrieval, tools, specialist agents, and backtesting.

This repository currently focuses on clean project foundations, not on implementing training, RAG, agents, or financial analysis logic.

## Repo Layout

```text
.
|-- AGENTS.md
|-- PROJECT_CONTEXT.md
|-- README.md
|-- configs/
|-- docs/
|-- scripts/
|-- src/
|   `-- stock_llm/
|       |-- agents/
|       |-- backtesting/
|       |-- data/
|       |-- models/
|       |-- rag/
|       |-- tools/
|       `-- training/
`-- tests/
```

## How To Run Tests

Create and activate a virtual environment, install dev dependencies, then run:

```powershell
python -m pip install -e .[dev]
python -m pytest
```

## How To Run Formatting And Linting

```powershell
python -m pip install -e .[dev]
python -m ruff format . --no-cache
python -m ruff check . --no-cache
```

## Coding Standards

- Prefer clear, boring code over clever abstractions.
- Keep files small and responsibilities narrow.
- Use type hints when they materially improve readability.
- Avoid adding dependencies unless they are needed now.
- Separate educational tiny-LLM work from practical finance system work.
- Use Python for deterministic calculations; do not rely on LLMs for arithmetic.
- Do not implement speculative architecture without an active milestone requiring it.

## Documentation Standards

- Update `README.md` when setup, workflow, or project scope changes.
- Add or update docs in `docs/` when architecture or design decisions become concrete.
- Document new commands in the relevant README or doc file.
- Keep examples minimal and runnable when possible.

## Branch And PR Expectations

- Work from feature branches, not directly on `main`.
- Prefer small, focused PRs with one clear purpose.
- Include tests for meaningful behavior changes.
- Document new dependencies, commands, or workflow changes in the PR.
- Keep generated diffs reviewable and avoid mixing unrelated cleanup.

## Required End-Of-Session Update

Every work session must end with an update to `PROJECT_CONTEXT.md` covering:

- What was created or changed
- Files changed
- Commands or tests run
- Important decisions
- Known issues or blockers
- Next 3 recommended tasks

## Repository Safety Rules

- Do not commit secrets, API keys, datasets, model checkpoints, or large generated artifacts.
- Do not commit `.env`, private credentials, paid data, or transient experiment outputs.
- Prefer external storage or explicit artifact management for large files.
