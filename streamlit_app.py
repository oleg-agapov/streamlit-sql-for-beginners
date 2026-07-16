from pathlib import Path

import streamlit as st

from components import lesson_title

ROOT = Path(__file__).parent

st.set_page_config(
    page_title="SQL from Scratch",
    page_icon=":material/database:",
    layout="wide",
    initial_sidebar_state="expanded",
)

pages = st.navigation(
    {
        "Start here": [
            st.Page(ROOT / "app_pages/home.py", title="Home", icon=":material/home:", default=True),
            st.Page(ROOT / "app_pages/course_map.py", title="Course map", icon=":material/map:"),
        ],
        "Chapter 1 · Foundations": [
            st.Page(
                ROOT / "app_pages/lesson_select.py",
                title=lesson_title("select", "1. Your first SELECT"),
                icon=":material/terminal:",
            ),
            st.Page(
                ROOT / "app_pages/lesson_filtering.py",
                title=lesson_title("filtering", "2. Filtering rows"),
                icon=":material/filter_alt:",
            ),
        ],
        "Coming next": [
            st.Page(ROOT / "app_pages/coming_soon.py", title="Joins & grouping", icon=":material/lock:"),
        ],
    },
    position="sidebar",
)

with st.sidebar:
    st.divider()
    st.caption("OPEN COURSE · BEGINNER FRIENDLY")

pages.run()
