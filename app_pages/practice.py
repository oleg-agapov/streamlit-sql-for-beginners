import streamlit as st

from sql_practice import DEFAULT_QUERY, STARTER_SQL, QueryError, execute_query

st.title("SQL practice")
st.markdown(
    "Run read-only queries against a fresh SQLite database. Every run starts from the same "
    "small `customers` and `orders` dataset, so experimenting is safe."
)

with st.expander("Dataset schema and starter rows"):
    st.code(STARTER_SQL, language="sql")
    st.download_button(
        "Download starter.sql",
        data=STARTER_SQL,
        file_name="starter.sql",
        mime="text/sql",
        icon=":material/download:",
    )

query = st.text_area("SQL query", value=DEFAULT_QUERY, height=260)
if st.button("Run query", type="primary", icon=":material/play_arrow:"):
    try:
        result = execute_query(query)
    except QueryError as error:
        st.error(f"SQLite says: {error}")
    else:
        records = [dict(zip(result.columns, row, strict=True)) for row in result.rows]
        st.success(f"Returned {len(records)} row{'s' if len(records) != 1 else ''}.")
        st.dataframe(records, width="stretch", hide_index=True)
        if result.truncated:
            st.warning("Showing the first 200 rows.")
