import streamlit as st

from course import load_course, module_name

st.title("Course map")
st.markdown("Follow the levels in order, or jump directly to the topic you need.")

modules = {}
for lesson in load_course():
    modules.setdefault(lesson.module, []).append(lesson)

for module, lessons in modules.items():
    complete = sum(bool(st.session_state.get(lesson.key)) for lesson in lessons)
    with st.container(border=True):
        left, right = st.columns([5, 1])
        left.markdown(f"#### {module_name(module)}")
        left.caption(" · ".join(lesson.title for lesson in lessons))
        right.metric("Progress", f"{complete}/{len(lessons)}")
        st.progress(complete / len(lessons))
