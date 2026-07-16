import pandas as pd
import streamlit as st

from components import completion, concept, learning_goals, lesson_header

lesson_header(1, "Your first SELECT", "Choose which columns you want to see from a table.", 8)
learning_goals("Recognize a table, row, and column", "Use `SELECT` and `FROM`", "Read a simple query from top to bottom")

st.markdown("### A table is a collection of facts")
st.markdown("Imagine a small `books` table. Each **row** is one book; each **column** describes it.")
books = pd.DataFrame(
    {"title": ["The Hobbit", "Kindred", "Piranesi", "Dune"], "author": ["J.R.R. Tolkien", "Octavia Butler", "Susanna Clarke", "Frank Herbert"], "pages": [310, 264, 272, 412]}
)
st.dataframe(books, hide_index=True, width="stretch")

st.markdown("### Ask for two columns")
st.code("SELECT title, author\nFROM books;", language="sql")
st.dataframe(books[["title", "author"]], hide_index=True, width="stretch")
concept("Why the semicolon?", "A semicolon marks the end of a SQL statement. Some tools make it optional, but it is a helpful habit.")

st.markdown("### Quick check")
answer = st.radio("Which keyword names the table?", ["Choose an answer", "SELECT", "FROM", "TABLE"], index=0)
if answer == "FROM":
    st.success("Correct. `FROM books` tells the database where to look.")
elif answer != "Choose an answer":
    st.error("Not quite. Look at the line immediately before the table name.")

completion("select")
