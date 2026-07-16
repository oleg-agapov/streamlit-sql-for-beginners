import streamlit as st


def lesson_title(key: str, title: str) -> str:
    suffix = " :green[:material/check_circle:]" if st.session_state.get(f"done_{key}") else ""
    return f"{title}{suffix}"


def lesson_header(number: int, title: str, summary: str, minutes: int) -> None:
    st.caption(f"CHAPTER 1 · LESSON {number}")
    st.title(title)
    st.markdown(summary)
    st.caption(f":material/schedule: About {minutes} minutes · No prior experience needed")
    st.divider()


def learning_goals(*goals: str) -> None:
    with st.container(border=True):
        st.markdown("#### :material/target: By the end, you can")
        for goal in goals:
            st.markdown(f"- {goal}")


def concept(title: str, body: str) -> None:
    with st.expander(f":material/lightbulb: {title}"):
        st.markdown(body)


def completion(key: str) -> None:
    st.divider()
    st.checkbox(
        "I finished this lesson",
        key=f"done_{key}",
        help="Your progress is kept for this browser session.",
    )
    if st.session_state.get(f"done_{key}"):
        st.success("Lesson complete — nice work! Choose the next lesson from the sidebar.")
