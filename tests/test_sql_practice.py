import unittest

from sql_practice import QueryError, execute_query


class SqlPracticeTests(unittest.TestCase):
    def test_query_returns_columns_and_rows(self) -> None:
        result = execute_query("SELECT name FROM customers ORDER BY id")
        self.assertEqual(("name",), result.columns)
        self.assertEqual(("Ada",), result.rows[0])
        self.assertEqual(4, len(result.rows))

    def test_database_is_read_only(self) -> None:
        with self.assertRaisesRegex(QueryError, "readonly"):
            execute_query("DELETE FROM customers RETURNING id")

    def test_multiple_statements_are_rejected(self) -> None:
        with self.assertRaisesRegex(QueryError, "one statement"):
            execute_query("SELECT 1; SELECT 2")

    def test_result_is_capped(self) -> None:
        result = execute_query(
            "WITH RECURSIVE n(x) AS "
            "(VALUES(1) UNION ALL SELECT x+1 FROM n WHERE x<10) "
            "SELECT x FROM n",
            row_limit=3,
        )
        self.assertEqual(3, len(result.rows))
        self.assertTrue(result.truncated)


if __name__ == "__main__":
    unittest.main()
