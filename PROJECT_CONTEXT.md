# Stock LLM Lab - AI Handoff Context

**Purpose:** This is the living context file for all AI chats and coding assistants that help with the Stock LLM Lab project. Paste this file into new chats or attach it to AI coding sessions so the assistant understands the project, current status, decisions, constraints, and next steps.

**How to update this file after every session:**
1. Update the **Current Status Snapshot**.
2. Add any new architectural or technical decisions to the **Decision Log**.
3. Update the **Active Milestone** and **Next 3 Tasks**.
4. Add new blockers, open questions, or risks.
5. Add a short note to the **Session Log**.
6. Keep this file concise enough to paste into a chat, but detailed enough that a new assistant can continue the project without starting over.

---

## 1. Project Summary

I am building a long-term learning and engineering project called **Stock LLM Lab**.

The goal is to learn how LLMs work by building a tiny GPT-style language model from scratch, then use that knowledge to build a more useful multi-agent stock research system. The final system should use financial data, SEC filings, textbook/RAG knowledge, Python-based calculations, specialist agents, and backtesting to produce structured investment research memos.

This is primarily a **learning and research project**, not a production financial advisory service.

### One-sentence explanation

Build a small LLM training pipeline from scratch for learning, then combine fine-tuned open-source models, retrieval, financial tools, and multi-agent debate to create a stock research assistant.

### What the system should eventually do

Given a stock ticker, the system should:

- Pull or load relevant company data.
- Parse financial statements and filings.
- Calculate key financial and market metrics in Python.
- Retrieve relevant finance/accounting/valuation knowledge from a document store.
- Ask multiple specialist agents to analyze the company from different angles.
- Force a bull case, bear case, valuation case, quant/risk view, and final committee decision.
- Produce a sourced, structured investment memo.
- Support historical backtesting without look-ahead bias.

### What the system should not claim to do

- It should not promise guaranteed stock-picking accuracy.
- It should not provide regulated personalized financial advice to others.
- It should not rely on LLMs for arithmetic or raw factual lookup when tools can do better.
- It should not make recommendations without uncertainty, sources, and risk discussion.

---

## 2. Current Status Snapshot

**Last updated:** 2026-06-27

**Current phase:** Repo setup / config system

**Current active milestone:** Milestone 0 - Project foundation

**Repository:** Local Git repo initialized in this workspace. Current working branch: `feature/config-system`. No remote is configured yet, so a real push/PR is still pending.

**Main working assumption:** Start with a small from-scratch model to learn the machinery. For the useful stock system, use open-source base models with RAG, tools, and eventually LoRA adapters.

**Current priority:** Build the minimal shared configuration layer before tokenizer or model work begins.

### Next 3 Tasks

1. Add CI to run `pytest` and `ruff` on every pull request.
2. Build the first dataset/tokenizer pipeline code against the new config loader.
3. Add config schemas for data processing once the first corpus workflow is defined.

### Current blockers

- No Git remote is configured yet, so the branch cannot be pushed and a real PR cannot be opened from this workspace alone.
- `ruff` requires `--no-cache` in this managed workspace because cache writes are denied. `pytest` now runs cleanly after disabling its cache plugin.

### Current open questions

- Should the repo keep the simplified package layout created here, or expand later toward the larger structure listed in Section 5?
- Which Python version should become the long-term baseline for contributors: 3.11 or newer?

---

## 3. Big-Picture Architecture

The project has two related tracks.

### Track A - Educational tiny LLM from scratch

Purpose: Learn the internals of language models.

Core components:

- Tokenizer training
- Dataset pipeline
- Decoder-only transformer
- Training loop
- Checkpointing
- Evaluation
- Text generation
- Experiment tracking

Expected result: A tiny finance-flavored GPT-style model that can generate semi-coherent financial text. It does not need to be useful for real stock research.

### Track B - Useful multi-agent stock research system

Purpose: Build a practical research assistant.

Core components:

- Financial data pipeline
- SEC filing ingestion
- Financial statement parsing
- Python calculation engine
- RAG over textbooks, notes, filings, and research documents
- Prompted specialist agents first
- Later: LoRA-trained specialist adapters
- Debate/committee orchestration
- Backtesting and evaluation

Expected result: A stock research memo generator and evaluation framework.

---

## 4. Proposed System Flow

```text
User asks about a stock ticker
        ↓
Data collector loads price history, filings, statements, transcripts, and metadata
        ↓
Python tools calculate ratios, growth, valuation metrics, volatility, drawdowns, etc.
        ↓
RAG layer retrieves relevant theory and source material
        ↓
Specialist agents analyze the stock:
  - Business quality agent
  - Financial statement agent
  - Valuation agent
  - Quant/risk agent
  - Macro/banking agent
  - Bear-case agent
        ↓
Committee agent compares arguments and produces final memo
        ↓
Backtester evaluates historical decisions against future returns and benchmarks
```

---

## 5. Recommended Repository Structure

```text
stock-llm-lab/
  README.md
  AGENTS.md
  PROJECT_CONTEXT.md
  pyproject.toml
  .env.example
  .gitignore
  docs/
    architecture.md
    roadmap.md
    data_sources.md
    evaluation.md
    decisions.md
  configs/
    tiny_gpt.yaml
    small_gpt.yaml
    rag.yaml
    agents.yaml
  data/
    README.md
    raw/
    processed/
    interim/
  notebooks/
  scripts/
    train_tokenizer.py
    pretrain_tiny_llm.py
    generate_text.py
    build_rag_index.py
    analyze_ticker.py
    run_backtest.py
  src/
    stock_llm/
      data/
      tokenizer/
      model/
      training/
      evaluation/
      rag/
      agents/
      finance/
      backtesting/
      utils/
  tests/
```

### Files that should never be committed

- `.env`
- API keys
- paid or restricted datasets
- large raw datasets
- model checkpoints unless intentionally tracked with Git LFS or external storage
- private financial data
- credentials, tokens, or cookies

---

## 6. GitHub Workflow

Use a traditional protected-main workflow.

### Branches

- `main`: stable branch only
- `feature/repo-bootstrap`
- `feature/tokenizer`
- `feature/tiny-transformer`
- `feature/training-loop`
- `feature/sec-loader`
- `feature/rag-index`
- `feature/valuation-agent`
- `feature/backtester`

### Pull request rules

A PR should include:

- Clear description of what changed
- Tests added or updated
- Any new commands documented
- No secrets committed
- No large generated artifacts committed accidentally
- Updated context file if the project direction changed

### Suggested development loop

```text
Create issue
Create feature branch
Implement small change
Run tests
Open PR
Review diff
Merge to main
Update PROJECT_CONTEXT.md / this handoff file
```

---

## 7. Milestone Roadmap

### Milestone 0 - Project foundation

Goal: Create the private GitHub repo and project skeleton.

Deliverables:

- Private repo created
- Protected `main` branch
- Python package layout
- `README.md`
- `AGENTS.md`
- `PROJECT_CONTEXT.md`
- `.env.example`
- Basic `pytest` setup
- Formatting/linting setup

Key concepts:

- Reproducibility
- Secret management
- Project structure
- Pull-request workflow
- Test-first habits

Exit criteria:

- `pytest` runs successfully
- A new AI assistant can read the context file and understand the project
- No secrets or large files are committed

---

### Milestone 1 - Dataset and tokenizer pipeline

Goal: Build the first data pipeline and tokenizer.

Deliverables:

- Small clean financial text corpus
- Data cleaning script
- Trainable tokenizer script
- Encode/decode tests
- Saved tokenizer artifact

Key concepts:

- Tokens
- Vocabulary size
- BPE or unigram tokenization
- Text normalization
- Train/validation split
- Data leakage prevention

Important notes:

- The tokenizer code and dataset pipeline matter more than early model quality.
- Keep the first corpus small and simple.
- Use only text that is legally allowed for training or experimentation.

Exit criteria:

- Text can be encoded into token IDs and decoded back into readable text.
- Tokenizer artifacts are saved in a reproducible way.
- Tests verify basic round-trip behavior.

---

### Milestone 2 - Tiny decoder-only transformer

Goal: Implement a small GPT-style model from scratch.

Deliverables:

- Token embeddings
- Positional embeddings
- Causal self-attention
- Feed-forward network
- Layer normalization
- Residual connections
- Output head
- Forward pass tests

Key concepts:

- Decoder-only transformer
- Attention masks
- Causal language modeling
- Cross-entropy loss
- Parameter count
- Context length

Suggested tiny config:

```yaml
model:
  vocab_size: 8000
  context_length: 256
  n_layers: 4
  n_heads: 4
  hidden_size: 256
  dropout: 0.1
```

Exit criteria:

- Model forward pass works.
- Output logits have expected shape.
- Loss can be calculated from input tokens.
- The model can overfit a tiny sample, proving the training path works.

---

### Milestone 3 - Pretraining loop

Goal: Train the tiny model with next-token prediction.

Deliverables:

- Training script
- Validation loop
- Checkpoint saving/loading
- Loss logging
- Text generation script
- Basic experiment log

Key concepts:

- Batching
- Optimizer
- Learning rate
- Warmup
- Gradient clipping
- Training loss vs validation loss
- Overfitting
- Checkpoints

Exit criteria:

- Training loss decreases.
- Validation loss is tracked.
- Checkpoints can be loaded.
- Model can generate text from a prompt.

---

### Milestone 4 - Evaluation harness

Goal: Create repeatable ways to judge model behavior.

Deliverables:

- Perplexity or validation loss reporting
- Simple generation benchmark prompts
- Regression tests for generation pipeline
- Experiment comparison table

Key concepts:

- Perplexity
- Validation loss
- Sampling temperature
- Top-k and top-p sampling
- Reproducibility seeds
- Model cards or experiment notes

Exit criteria:

- Experiments can be compared across runs.
- Model changes are not judged only by vibes.
- Training runs produce logs and metrics.

---

### Milestone 5 - RAG foundation

Goal: Build retrieval over project documents, textbooks, notes, and filings.

Deliverables:

- Document ingestion script
- Chunking strategy
- Embedding pipeline
- Vector store
- Retrieval test script
- Example question-answer flow using retrieved context

Key concepts:

- Chunk size
- Overlap
- Embeddings
- Vector similarity
- Retrieval precision
- Source attribution
- Hallucination reduction

Exit criteria:

- Given a finance question, the system retrieves relevant chunks.
- Answers can include citations or source references.
- The system can separate retrieved facts from model-generated interpretation.

---

### Milestone 6 - Financial data and calculation engine

Goal: Make Python responsible for financial facts and math.

Deliverables:

- Structured ticker analysis JSON
- Basic price-history loader
- Financial statement schema
- Ratio calculation functions
- Unit tests for financial formulas

Metrics to calculate:

- Revenue growth
- Gross margin
- Operating margin
- Net margin
- Free cash flow margin
- Debt / EBITDA
- Return on invested capital
- P/E
- EV / EBITDA
- Free cash flow yield
- Volatility
- Max drawdown
- Momentum

Key concepts:

- Structured data
- Financial statement normalization
- Time series alignment
- Data quality checks
- Avoiding hallucinated numbers

Exit criteria:

- `analyze_ticker("AAPL")` or equivalent returns structured metrics.
- Ratios are calculated by code, not by the LLM.
- Tests validate core formulas.

---

### Milestone 7 - Prompt-based specialist agents

Goal: Build the first multi-agent system without training adapters yet.

Deliverables:

- Business quality agent
- Financial statement agent
- Valuation agent
- Quant/risk agent
- Macro/banking agent
- Bear-case agent
- Final committee agent
- Structured JSON output format

Key concepts:

- Agent roles
- Prompt design
- Structured outputs
- Forced disagreement
- Confidence calibration
- Evidence-based reasoning

Required agent output format:

```json
{
  "rating": "buy / hold / avoid / insufficient_data",
  "confidence": 0.0,
  "top_reasons": [],
  "risks": [],
  "evidence_used": [],
  "missing_information": []
}
```

Exit criteria:

- Given a ticker and structured metrics, agents produce separate analyses.
- The bear-case agent can disagree with the bull case.
- The committee agent can choose `insufficient_data` instead of forcing a recommendation.

---

### Milestone 8 - Backtesting framework

Goal: Evaluate whether the research process has predictive value.

Deliverables:

- Historical decision dates
- Data availability filters
- Backtest runner
- Benchmark comparison
- Return/risk metrics
- Backtest report

Key concepts:

- Look-ahead bias
- Survivorship bias
- Data leakage
- Benchmarking
- Transaction costs
- Risk-adjusted returns
- Out-of-sample testing

Critical rule:

The model must only see information that was available on the decision date. Future filings, future prices, and future index membership must not leak into the prompt.

Exit criteria:

- The backtester can simulate historical recommendations.
- Performance is compared against a benchmark.
- The test clearly documents what information was available at the time.

---

### Milestone 9 - Fine-tuning and LoRA adapters

Goal: Train specialist model behavior after the system already works with prompts.

Deliverables:

- Instruction dataset format
- Valuation training set
- Bear-case training set
- Financial statement analysis training set
- LoRA fine-tuning script
- Evaluation script comparing base model vs adapter

Key concepts:

- Supervised fine-tuning
- LoRA / QLoRA
- Dataset quality
- Instruction formatting
- Overfitting
- Adapter merging/loading
- Behavior evaluation

Suggested adapter plan:

- `valuation_adapter`
- `accounting_adapter`
- `quant_risk_adapter`
- `bear_case_adapter`
- `committee_adapter`

Exit criteria:

- At least one specialist adapter is trained.
- The adapter is compared against the base model on a held-out evaluation set.
- The adapter improves a targeted behavior, not just style.

---

### Milestone 10 - Paper trading and continuous evaluation

Goal: Track model decisions prospectively.

Deliverables:

- Paper-trading log
- Decision memo archive
- Confidence tracking
- Monthly evaluation report
- Error analysis process

Key concepts:

- Prospective evaluation
- Decision journaling
- Calibration
- Error analysis
- Model drift
- Human review

Exit criteria:

- The system logs recommendations before outcomes are known.
- Future performance is measured honestly.
- Mistakes are categorized and used to improve the system.

---

## 8. Key Technical Principles

### Use LLMs for reasoning, not arithmetic

Python should calculate financial metrics. LLMs should interpret, critique, summarize, and explain.

### Train for intermediate skill, not magic stock picks

Do not train models only to output `buy` or `sell`. Train them to:

- Extract risks from filings
- Summarize financial deterioration
- Explain valuation assumptions
- Identify missing data
- Generate bear cases
- Compare evidence
- Communicate uncertainty

### Retrieval before fine-tuning

Use RAG when the model needs access to documents. Use fine-tuning when the model needs to behave differently or follow a specialized reasoning pattern.

### Backtesting is mandatory

Without backtesting, this is only a fancy memo generator. Backtesting turns it into a research system.

### Avoid false precision

The system should not pretend to know the future. Confidence scores should be conservative and supported by evidence.

---

## 9. Data Policy and Safety Notes

### Allowed data examples

- SEC filings
- Company facts and public financial statements
- Public price data where terms allow usage
- Public-domain textbooks or notes
- User-created notes
- Properly licensed datasets

### Be careful with

- Copyrighted textbooks
- Paid financial datasets
- Earnings transcript licensing
- Redistribution rights
- API terms of service

### Compliance boundary

This project should be described as a research and learning tool. Avoid presenting it as a regulated financial adviser or as personalized investment advice.

---

## 10. Decision Log

Use this section to record important choices so future AI chats do not revisit the same debate unnecessarily.

| Date | Decision | Reason | Status |
|---|---|---|---|
| YYYY-MM-DD | Use private GitHub repo | Protect keys, data, and experiments | Planned |
| YYYY-MM-DD | Build tiny LLM from scratch for learning | Learn tokenizer, transformer, and training loop internals | Planned |
| YYYY-MM-DD | Use open-source models + RAG + tools for useful system | More realistic than pretraining a large model from scratch | Planned |
| YYYY-MM-DD | Use PR-based workflow into protected main | Keep project stable and reviewable | Planned |
| 2026-06-27 | Start with a minimal Python package skeleton and `ruff` + `pytest` tooling | Establish a clean, boring foundation before implementation | Completed |
| 2026-06-27 | Initialize Git locally and work from `feature/project-foundation` | Align the workspace with the documented feature-branch workflow | Completed |
| 2026-06-27 | Use dataclasses plus a small YAML loader for configs | Keep configuration typed and readable without introducing a heavy framework | Completed |
| 2026-06-27 | Add `PyYAML` as the only new runtime dependency for configs | YAML loading is required and Python has no standard-library YAML parser | Completed |

---

## 11. Active Work Board

### Now

- [x] Create repo skeleton
- [x] Add AGENTS.md
- [x] Add PROJECT_CONTEXT.md
- [x] Set up Python environment
- [x] Add basic tests
- [x] Add initial typed config system

### Next

- [ ] Build initial corpus loader
- [ ] Train first tokenizer
- [ ] Implement tiny transformer forward pass
- [ ] Add checkpointing
- [ ] Add basic generation script

### Later

- [ ] Build RAG layer
- [ ] Add SEC filing ingestion
- [ ] Add financial calculation engine
- [ ] Build prompt-based agents
- [ ] Build backtester
- [ ] Train first LoRA adapter

---

## 12. AI Assistant Instructions

When helping with this project, the assistant should:

- Treat the project as a serious engineering and learning project.
- Prefer small, testable steps over giant rewrites.
- Keep the protected-main PR workflow in mind.
- Explain technical concepts when introducing them.
- Suggest tests for every meaningful feature.
- Avoid committing secrets or large datasets.
- Prefer config-driven code so tiny/small/medium models can use the same pipeline.
- Separate educational from-scratch LLM work from the useful stock research system.
- Use Python for financial calculations instead of asking the LLM to do math.
- Keep backtesting and data leakage prevention in mind from the start.
- Update this handoff file when project direction or current status changes.

### Assistant should not

- Claim the system can guarantee stock returns.
- Recommend using copyrighted textbooks without checking rights.
- Encourage skipping evaluation or backtesting.
- Hard-code one-off paths when a config would be better.
- Suggest training a huge model from scratch before the tiny pipeline works.

---

## 13. Standard Prompt for a New AI Chat

Paste this prompt at the start of a new chat, then attach or paste this file.

```text
I am working on a project called Stock LLM Lab. It is a long-term learning and engineering project where I will build a tiny GPT-style LLM from scratch to learn the internals, then build a useful multi-agent stock research assistant using open-source models, RAG, financial data tools, specialist agents, and backtesting.

Please read the attached project handoff file before giving advice. Keep recommendations aligned with the current milestones, decision log, and repository workflow. I want small, testable steps that can be added through pull requests into a private GitHub repo. When suggesting code, include tests and avoid secrets or large committed artifacts. If we make decisions or complete work, help me update the handoff file at the end of the session.
```

---

## 14. Session Log

Use one short entry per work session.

### 2026-06-27 - Project foundation bootstrap

**Worked on:**

- Created the initial repository skeleton for package code, docs, configs, scripts, and tests.
- Added repository conventions, setup docs, quality-tool configuration, and safety guardrails.
- Initialized local Git and created the `feature/project-foundation` branch.
- Installed dev dependencies and ran the initial test and lint checks.

**Decisions made:**

- Use `ruff` for linting and formatting, with `pytest` for the initial test runner.
- Keep the first package layout small and aligned to current milestones rather than prebuilding deeper abstractions.
- Use a local Git repo immediately even before a remote is connected, so feature-branch workflow can start now.
- Run `ruff` with `--no-cache` in this workspace because local cache writes fail under the current filesystem permissions.

**Files changed:**

- `AGENTS.md`
- `README.md`
- `pyproject.toml`
- `.env.example`
- `.gitignore`
- `PROJECT_CONTEXT.md`
- `configs/README.md`
- `docs/architecture.md`
- `scripts/README.md`
- `src/stock_llm/__init__.py`
- `src/stock_llm/data/__init__.py`
- `src/stock_llm/models/__init__.py`
- `src/stock_llm/training/__init__.py`
- `src/stock_llm/rag/__init__.py`
- `src/stock_llm/agents/__init__.py`
- `src/stock_llm/backtesting/__init__.py`
- `src/stock_llm/tools/__init__.py`
- `tests/test_placeholder.py`
- Local Git metadata initialized in `.git/`

**Next steps:**

- Add a remote, push `feature/project-foundation`, and open the first PR.
- Wire up CI for `pytest` and `ruff`.

**Open questions/blockers:**

- No remote repository is configured yet, so a real PR still cannot be opened from this workspace.
- `ruff` cache writes are blocked in this workspace, so local contributors should use `--no-cache` unless permissions change.

### 2026-06-27 - Config system bootstrap

**Worked on:**

- Added `stock_llm.config` with typed dataclass schemas and YAML loading helpers.
- Added starter YAML configs for tokenizer, model, and training settings.
- Added config loader tests for valid, missing, and invalid config cases.
- Updated README guidance for the new config workflow.

**Decisions made:**

- Use standard-library dataclasses for typed schemas to keep the system simple.
- Add `PyYAML` as the only new dependency because YAML support is required and not available in the Python standard library.
- Keep config files flat and explicit for now instead of designing a generic nested config framework early.

**Files changed:**

- `README.md`
- `pyproject.toml`
- `PROJECT_CONTEXT.md`
- `configs/README.md`
- `configs/tokenizer_tiny.yaml`
- `configs/model_tiny.yaml`
- `configs/training_tiny.yaml`
- `src/stock_llm/config/__init__.py`
- `src/stock_llm/config/schema.py`
- `src/stock_llm/config/loader.py`
- `tests/test_config_loader.py`
- `tests/fixtures/invalid_model.yaml`

**Commands/tests run:**

- `python -m pip install -e .[dev]`
- `python -m pytest`
- `python -m ruff check . --no-cache`
- `python -m ruff format --check . --no-cache`

**Important decisions:**

- The loader validates field presence, unknown fields, basic scalar types, and schema-level value checks.
- Config loading supports either names from `configs/` or explicit file paths.

**Known issues:**

- No remote repository is configured yet, so the branch still cannot be pushed or opened as a PR from this workspace alone.
- `ruff` still needs `--no-cache` in this managed environment.

**Next steps:**

- Add CI so config validation and tests run automatically on PRs.
- Build the first tokenizer/data pipeline code against `TokenizerConfig`.
- Decide whether later configs should stay flat or introduce grouped nested sections when the training loop exists.

---

## 15. Glossary

**Backtesting:** Testing a strategy on historical data while only using information that would have been available at the time.

**Causal language modeling:** Training a model to predict the next token from previous tokens.

**Decoder-only transformer:** GPT-style architecture used for next-token prediction and text generation.

**Embedding:** Numeric representation of text used for similarity search.

**Fine-tuning:** Further training an existing model on a specific dataset or behavior.

**LoRA:** Parameter-efficient fine-tuning method that trains small adapter weights instead of all base model weights.

**Look-ahead bias:** Accidentally using future information in a historical test.

**RAG:** Retrieval-augmented generation; retrieving relevant documents and giving them to the model as context.

**Tokenizer:** Component that converts text into token IDs and token IDs back into text.

---

## 16. Compact Context Version

Use this if an AI chat has a short context window.

```text
Project: Stock LLM Lab.
Goal: Learn LLM internals by building a tiny GPT-style model from scratch, then build a practical multi-agent stock research assistant using open-source models, RAG, financial data tools, specialist agents, and backtesting.

Important decisions:
- Use private GitHub repo with protected main and PRs.
- Build tiny LLM from scratch for learning, not for production stock picking.
- Use open-source base models + RAG + Python tools for the useful system.
- Later train LoRA adapters for specialist agents.
- Python calculates financial metrics; LLMs interpret and critique.
- Backtesting must avoid look-ahead bias and survivorship bias.

Current milestone: [fill in]
Next tasks: [fill in]
Current blockers: [fill in]

Preferred assistant behavior:
Give small, testable steps. Include tests. Avoid secrets and large committed files. Keep repo workflow in mind. Update this context file after major decisions.
```
