from pathlib import Path

import streamlit as st

from course import create_lesson_page, lesson_nav_title, load_course, module_name

ROOT = Path(__file__).parent

st.set_page_config(
    page_title="SQL from Scratch",
    page_icon=":material/database:",
    layout="wide",
    initial_sidebar_state="expanded",
)

navigation = {
    "Start here": [
        st.Page(ROOT / "app_pages/home.py", title="Home", icon=":material/home:", default=True),
        st.Page(ROOT / "app_pages/course_map.py", title="Course map", icon=":material/map:"),
    ]
}

for lesson in load_course():
    section = module_name(lesson.module)
    navigation.setdefault(section, []).append(
        st.Page(
            create_lesson_page(lesson),
            title=lesson_nav_title(lesson),
            icon=":material/terminal:",
            url_path=lesson.route.lstrip("/"),
        )
    )

pages = st.navigation(navigation, position="sidebar")

with st.sidebar:
    st.divider()
    st.caption("OPEN COURSE · BEGINNER FRIENDLY")

pages.run()
