# SQL from Scratch

A beginner-friendly, open SQL course built with Streamlit. It includes 42 short lessons,
same-tab navigation, URL-backed progress, and a safe SQLite practice area with downloadable
starter data.

## Requirements

- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- Python 3.10 or newer (uv can install it when needed)
- Streamlit 1.52, resolved in `uv.lock`

## Run locally

```bash
make dev
```

The `dev` target syncs the locked uv environment and starts the Streamlit development server.

Open **SQL practice** in the app to run read-only queries against the included `customers` and
`orders` tables. Each run uses a fresh in-memory SQLite database.

## Develop and test

```bash
uv sync
uv run ruff check .
uv run python -m unittest discover -s tests -v
```

`uv sync` installs the application and default `dev` dependency group into `.venv`. Commit changes
to both `pyproject.toml` and `uv.lock` whenever dependencies change. Use `uv lock --check` to verify
that the lockfile is current without modifying it.

CI runs linting, unit tests, and a Streamlit startup smoke test on Python 3.10 and 3.12.

## Add or edit a lesson

Lessons live under `app_pages/lessons/module-*/` and use this format:

```markdown
---
title: Selecting rows
module: 1 — Basics
order: 1
level: 1
minutes: 5
---

# Selecting rows

Lesson content...
```

Required metadata fields are `title`, `module`, `order`, `level`, and `minutes`. Filenames must
follow `<order>-<slug>.md`. Routes and `(level, order)` progress keys must be unique. The loader
validates the full course at startup and reports the offending path when content is invalid.

## Deployment

Use `streamlit_app.py` as the entry point. Install the locked dependencies and run:

```bash
uv sync --locked --no-dev
uv run --no-dev streamlit run streamlit_app.py --server.headless=true
```

Completion state is stored in the `completed` URL query parameter. Learners can bookmark or share
that URL; no account or server-side database is required.

## Project structure

- `streamlit_app.py` builds grouped multipage navigation.
- `pyproject.toml` declares project and development dependencies; `uv.lock` resolves them.
- `course.py` loads, validates, and renders Markdown lessons.
- `sql_practice.py` owns the disposable SQLite practice engine.
- `app_pages/` contains the home, map, practice page, and lesson content.
- `tests/` covers lesson validation and SQL sandbox behavior.
