.PHONY: dev

dev:
	uv sync --locked
	uv run streamlit run streamlit_app.py
