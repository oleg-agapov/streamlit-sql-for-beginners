import streamlit as st

from course import load_course

lessons = load_course()
total_minutes = sum(lesson.minutes for lesson in lessons)

st.caption("A FREE, HANDS-ON COURSE")
st.title("Learn SQL from scratch")
st.markdown(
    "A practical introduction to asking useful questions of data — one small query at a time."
)

st.space("small")
col1, col2, col3 = st.columns(3)
col1.metric("Levels", "5", help="Plus a short getting-started module")
col2.metric("Lessons", str(len(lessons)))
col3.metric("Study time", f"~{total_minutes // 60} hours")

st.space("medium")
left, right = st.columns([3, 2], gap="large")
with left:
    st.markdown("### What you’ll learn")
    st.markdown(
        """
        Start with tables, rows, and columns. Then learn to filter, summarize, and combine data;
        use window functions; design database structures; and develop practical optimization
        habits. The lessons are short enough to complete with a query editor open beside them.
        """
    )
    st.link_button(
        "Start the course →", lessons[0].route, type="primary", width="stretch"
    )

with right:
    with st.container(border=True):
        st.markdown("#### :material/database: The core idea")
        st.markdown("SQL lets you describe **the result you want**. The database figures out how to retrieve it.")
        st.code("SELECT name, city\nFROM customers;", language="sql")

st.space("medium")
st.markdown("### How the course works")
a, b, c = st.columns(3)
with a:
    with st.container(border=True):
        st.markdown("#### 1 · Learn")
        st.caption("Meet one idea at a time in plain language.")
with b:
    with st.container(border=True):
        st.markdown("#### 2 · Try")
        st.caption("Run each example in your own SQLite query editor.")
with c:
    with st.container(border=True):
        st.markdown("#### 3 · Progress")
        st.caption("Mark lessons complete as you build confidence.")
