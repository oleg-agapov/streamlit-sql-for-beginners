import streamlit as st

st.title("Course map")
st.markdown("The first chapter is ready. Later chapters show the intended direction of the course.")

for title, status, lessons in [
    ("1 · Foundations", "Available", "SELECT · WHERE · ORDER BY"),
    ("2 · Summarizing data", "Planned", "COUNT · SUM · GROUP BY"),
    ("3 · Combining tables", "Planned", "Keys · INNER JOIN · LEFT JOIN"),
    ("4 · Practical SQL", "Planned", "CASE · Dates · A small analysis project"),
]:
    with st.container(border=True):
        left, right = st.columns([4, 1])
        left.markdown(f"#### {title}")
        left.caption(lessons)
        right.markdown(f"`{status}`")
