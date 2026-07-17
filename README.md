# SQL from Scratch

A beginner-friendly, open SQL course built with Streamlit.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run streamlit_app.py
```

The app loads 42 short Markdown lessons from `app_pages/lessons/` and builds grouped sidebar
navigation for all six modules. Lessons are grouped into module folders and rendered through one
shared callable page component, while retaining stable routes, previous/next navigation, and
per-session completion state.
