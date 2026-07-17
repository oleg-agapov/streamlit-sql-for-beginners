# AGENTS.md

## Project overview

This repository contains **SQL from Scratch**, a beginner-friendly Streamlit course. The app
builds navigation from Markdown lessons, tracks completion in URL query parameters, and includes
a disposable, read-only SQLite practice environment.

## Development commands

- Start the development server: `make dev`
- Sync the locked environment: `uv sync --locked`
- Lint: `uv run ruff check .`
- Run tests: `uv run python -m unittest discover -s tests -v`
- Verify the lockfile: `uv lock --check`

Run linting and tests after changing Python code. Update both `pyproject.toml` and `uv.lock` when
dependencies change. Do not add `requirements.txt`; uv is the project's dependency manager.

## Repository structure

- `streamlit_app.py` configures the application and grouped multipage navigation.
- `course.py` parses, validates, and renders lessons and manages progress state.
- `sql_practice.py` contains the isolated SQLite practice engine and starter dataset.
- `app_pages/` contains Streamlit pages and Markdown lessons.
- `tests/` contains the standard-library `unittest` suite.
- `.github/workflows/ci.yml` defines lint, test, and startup checks.

## Lesson authoring

Lessons live in `app_pages/lessons/module-*/` and must be named `<order>-<slug>.md`. Each lesson
must begin with exactly these front-matter fields:

```yaml
---
title: Lesson title
module: 1 — Basics
order: 1
level: 1
minutes: 5
---
```

Keep `(level, order)` pairs and generated routes unique. The `module` number must match `level`,
and `order` and `minutes` must be positive integers. Lessons should use short explanations,
portable SQL where practical, fenced `sql` examples, and an explicit exercise or takeaway.

When adding or removing lessons, update the expected lesson count in `tests/test_course.py` and
any README text that states the count.

## Implementation guidelines

- Preserve same-session navigation with `st.page_link`; do not use `st.link_button` for internal
  pages.
- Pass the current progress query parameters to internal page links.
- Keep Streamlit-specific rendering in page modules or `course.py`; keep reusable logic testable
  without starting a server.
- The SQL practice database must remain fresh per execution and read-only before user SQL runs.
- Do not permit persistent writes, filesystem-attached SQLite databases, or unrestricted scripts
  in the practice engine.
- Add or update tests for parser rules, progress behavior, and SQL sandbox changes.
- Keep compatibility with Python 3.10 and the Streamlit version pinned in `pyproject.toml`.

## Before handing off changes

Run:

```bash
uv lock --check
uv run ruff check .
uv run python -m unittest discover -s tests -v
```

Also run `git diff --check` and inspect `git status` so unrelated user changes are preserved.
