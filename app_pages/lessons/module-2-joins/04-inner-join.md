---
title: Your First JOIN (INNER JOIN)
module: 2 — Joins
order: 4
level: 2
minutes: 7
---

# Your First JOIN (INNER JOIN)

**Joins combine two tables based on a relationship between them.** Where subqueries and unions are occasional tools, joins are *the* everyday way to bring two tables into one result set.

A few ground rules:

- Joins happen between **two tables**, usually called the *left* and *right* tables.
- One query can have zero, one, or many joins.
- Tables are joined on a **common column** — a relation. (That shared-key idea is why these are called *relational* databases.)

## A worked example

**Task:** the finance team wants orders and gross revenue broken down by country and year:

```
report_year | country | orders | gross_revenue
------------+---------+--------+--------------
```

First, find the sources:

- `report_year`, `orders`, `gross_revenue` → from `payments`
- `country` → only in `users`

How are the tables connected? Through `payments.user_id = users.id`. That's our join key.

Let's start with the simplest possible join:

```sql
SELECT *
FROM payments
JOIN users ON users.id = payments.user_id;
```

Syntax notes:

- `JOIN` comes right after `FROM`
- then the table to join
- then `ON` with the join condition (the matching keys)
- prefix columns with the table name, since both tables may share column names

The result attaches each payment's matching user row side by side.

## The full solution

```sql
SELECT
  strftime('%Y', payments.event_date) AS report_year,
  users.country,
  count(payments.id) AS orders,
  sum(payments.gross_revenue) AS gross_revenue
FROM payments
JOIN users ON users.id = payments.user_id
GROUP BY 1, 2
ORDER BY 1, 2;
```

Step by step:

1. `payments` is the main table.
2. We join `users` on the user's ID.
3. With both tables combined, we can group and aggregate across columns from either.

This is an **inner join**: the result contains **only rows that match in both tables**. Some databases let you write it explicitly:

```sql
FROM table_1
INNER JOIN table_2 ON ...
```

`JOIN` and `INNER JOIN` mean the same thing.

---

> 💡 **Try it:** Join `payments` to `users` and list `first_name` next to each `gross_revenue`.

➡️ Next: **Keeping unmatched rows with LEFT JOIN**
