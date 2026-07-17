import streamlit as st

from course import load_course, module_name, page_for, progress_query

st.title("Course map")
st.markdown("Follow the levels in order, or jump directly to the topic you need.")

all_lessons = load_course()
query = progress_query(all_lessons)
modules = {}
for lesson in all_lessons:
    modules.setdefault(lesson.module, []).append(lesson)

for module, lessons in modules.items():
    complete = sum(bool(st.session_state.get(lesson.key)) for lesson in lessons)
    with st.container(border=True):
        left, right = st.columns([5, 1])
        left.markdown(f"#### {module_name(module)}")
        right.metric("Progress", f"{complete}/{len(lessons)}")
        st.progress(complete / len(lessons))
        for lesson in lessons:
            icon = (
                ":material/check_circle:"
                if st.session_state.get(lesson.key)
                else ":material/terminal:"
            )
            st.page_link(
                page_for(lesson),
                label=f"{lesson.order}. {lesson.title} · {lesson.minutes} min",
                icon=icon,
                width="stretch",
                query_params=query,
            )
