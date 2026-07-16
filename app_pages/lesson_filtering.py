import pandas as pd
import streamlit as st

from components import completion, concept, learning_goals, lesson_header

lesson_header(2, "Filtering rows with WHERE", "Return only the rows that match a condition.", 10)
learning_goals("Add a `WHERE` clause", "Compare numeric values", "Predict which rows a filter returns")

books = pd.DataFrame(
    {"title": ["The Hobbit", "Kindred", "Piranesi", "Dune"], "author": ["J.R.R. Tolkien", "Octavia Butler", "Susanna Clarke", "Frank Herbert"], "pages": [310, 264, 272, 412]}
)

st.markdown("### Keep only matching rows")
st.markdown("`WHERE` works like a gate: a row appears only when its condition is true.")
st.code("SELECT title, pages\nFROM books\nWHERE pages >= 300;", language="sql")

st.markdown("### Try the filter")
minimum = st.slider("Minimum page count", min_value=200, max_value=450, value=300, step=10)
st.code(f"SELECT title, pages\nFROM books\nWHERE pages >= {minimum};", language="sql")
result = books.loc[books["pages"] >= minimum, ["title", "pages"]]
st.dataframe(result, hide_index=True, width="stretch")
st.caption(f"{len(result)} row{'s' if len(result) != 1 else ''} returned")

concept("Common comparison operators", "Use `=` for equal, `<>` for not equal, `>` or `<` for comparisons, and `>=` or `<=` to include the boundary.")
completion("filtering")
