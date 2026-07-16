import streamlit as st

st.caption("A FREE, HANDS-ON COURSE")
st.title("Learn SQL from scratch")
st.markdown(
    "A practical introduction to asking useful questions of data — one small query at a time."
)

st.space("small")
col1, col2, col3 = st.columns(3)
col1.metric("Level", "Beginner", help="No SQL experience required")
col2.metric("Available now", "2 lessons")
col3.metric("Format", "Learn + practice")

st.space("medium")
left, right = st.columns([3, 2], gap="large")
with left:
    st.markdown("### What you’ll learn")
    st.markdown(
        """
        Start with the vocabulary of tables, rows, and columns. Then write queries that select,
        filter, sort, summarize, and combine data. Every lesson pairs a short explanation with
        examples and a low-stakes exercise.
        """
    )
    st.page_link("app_pages/lesson_select.py", label="Start lesson 1", icon=":material/arrow_forward:")

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
        st.caption("Change a query and see its result immediately.")
with c:
    with st.container(border=True):
        st.markdown("#### 3 · Progress")
        st.caption("Mark lessons complete as you build confidence.")
