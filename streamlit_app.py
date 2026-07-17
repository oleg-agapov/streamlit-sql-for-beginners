from pathlib import Path

import streamlit as st

from course import (
    create_lesson_page,
    initialize_progress,
    lesson_nav_title,
    load_course,
    module_name,
    register_page,
    save_progress,
)

ROOT = Path(__file__).parent

st.set_page_config(
    page_title="SQL from Scratch",
    page_icon=":material/database:",
    layout="wide",
    initial_sidebar_state="expanded",
)

lessons = load_course()
initialize_progress(lessons)
save_progress(lessons)
navigation = {
    "Start here": [
        st.Page(ROOT / "app_pages/home.py", title="Home", icon=":material/home:", default=True),
        st.Page(ROOT / "app_pages/course_map.py", title="Course map", icon=":material/map:"),
        st.Page(ROOT / "app_pages/practice.py", title="SQL practice", icon=":material/play_arrow:"),
    ]
}

for lesson in lessons:
    section = module_name(lesson.module)
    page = st.Page(
        create_lesson_page(lesson),
        title=lesson_nav_title(lesson),
        icon=":material/terminal:",
        url_path=lesson.route,
    )
    register_page(lesson.route, page)
    navigation.setdefault(section, []).append(page)

pages = st.navigation(navigation, position="sidebar")

with st.sidebar:
    st.divider()
    st.caption("OPEN COURSE · BEGINNER FRIENDLY")

pages.run()
