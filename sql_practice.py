from __future__ import annotations

import sqlite3
from dataclasses import dataclass

STARTER_SQL = """\
CREATE TABLE customers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    city TEXT NOT NULL,
    signup_date TEXT NOT NULL
);

CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL REFERENCES customers(id),
    total REAL NOT NULL,
    ordered_at TEXT NOT NULL
);

INSERT INTO customers VALUES
    (1, 'Ada', 'London', '2024-01-10'),
    (2, 'Linus', 'Helsinki', '2024-02-18'),
    (3, 'Grace', 'New York', '2024-03-05'),
    (4, 'Margaret', 'New York', '2024-04-22');

INSERT INTO orders VALUES
    (1, 1, 49.00, '2024-05-01'),
    (2, 1, 25.50, '2024-05-12'),
    (3, 2, 99.99, '2024-06-03'),
    (4, 4, 15.00, '2024-06-15');
"""

DEFAULT_QUERY = """\
SELECT
  customers.name,
  COUNT(orders.id) AS order_count,
  COALESCE(SUM(orders.total), 0) AS lifetime_value
FROM customers
LEFT JOIN orders ON orders.customer_id = customers.id
GROUP BY customers.id, customers.name
ORDER BY lifetime_value DESC;
"""


class QueryError(ValueError):
    """A safe, user-facing SQL execution error."""


@dataclass(frozen=True)
class QueryResult:
    columns: tuple[str, ...]
    rows: tuple[tuple[object, ...], ...]
    truncated: bool = False


def execute_query(query: str, row_limit: int = 200) -> QueryResult:
    """Execute one query against a fresh, disposable SQLite database."""

    if not query.strip():
        raise QueryError("Write a query before pressing Run.")
    connection = sqlite3.connect(":memory:")
    try:
        connection.executescript(STARTER_SQL)
        connection.execute("PRAGMA query_only = ON")
        try:
            cursor = connection.execute(query)
        except sqlite3.Error as error:
            raise QueryError(str(error)) from error
        if cursor.description is None:
            raise QueryError("The practice area accepts queries that return rows.")
        rows = cursor.fetchmany(row_limit + 1)
        return QueryResult(
            columns=tuple(column[0] for column in cursor.description),
            rows=tuple(rows[:row_limit]),
            truncated=len(rows) > row_limit,
        )
    finally:
        connection.close()
