---
title: A Trap — Row Duplication in Joins
module: 2 — Joins
order: 6
level: 2
minutes: 5
---

# A Trap — Row Duplication in Joins

Here's a gotcha that bites everyone eventually.

**What happens if the joined table has more than one matching row?** The join *duplicates* the main-table row once for each match.

Picture one user:

```
user_id | first_name
--------+-----------
      1 | John
```

…who made two purchases:

```
order_id | gross_revenue | user_id
---------+---------------+--------
       1 |         29.99 |       1
       2 |         49.99 |       1
```

Join them (using a little CTE + UNION to fabricate the tables):

```sql
WITH table_users AS (
  SELECT 1 AS user_id, 'John' AS first_name
),
table_orders AS (
  SELECT 1 AS order_id, 29.99 AS gross_revenue, 1 AS user_id
  UNION
  SELECT 2 AS order_id, 49.99 AS gross_revenue, 1 AS user_id
)
SELECT *
FROM table_users
JOIN table_orders ON table_orders.user_id = table_users.user_id;
```

Result:

```
user_id | first_name | order_id | gross_revenue | user_id
--------+------------+----------+---------------+--------
      1 | John       |        1 |         29.99 |       1
      1 | John       |        2 |         49.99 |       1
```

John's row appears **twice** — once per matching order.

## Why this matters

This is exactly what you *want* when listing each order with its user. But it's a silent bug when you forget it — for example, joining before aggregating can inflate a `count()` or `sum()` because rows got multiplied.

Rule of thumb: **always know the "grain" of your join.** Ask yourself how many rows a single left-table row can match. If it's more than one, your totals may be multiplied.

---

> 💡 **Watch for it:** Whenever a count looks suspiciously high after a join, suspect duplication first.

➡️ Next: **CROSS JOIN and the Cartesian product**
