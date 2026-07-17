---
title: Subqueries — Queries Inside Queries
module: 2 — Joins
order: 1
level: 2
minutes: 7
---

# Subqueries — Queries Inside Queries

Basic SQL handles one table at a time. But real questions often span two tables. The first tool for combining them is the **subquery**.

**A subquery is a query nested inside another query.** They can appear in `SELECT`, `FROM`, or `WHERE`.

> Subqueries often solve the same problems as joins (coming up next). Sometimes a join is cleaner — but understanding subqueries first makes joins click.

## Example 1 — subquery in SELECT

Get each user's name plus their total spending:

```sql
SELECT
  first_name,
  last_name,
  (SELECT sum(gross_revenue)
   FROM payments p
   WHERE p.user_id = u.id) AS total_spendings
FROM users u;
```

This subquery runs **once per row** of the outer query — once for every user. Two rules keep it valid:

- it must return exactly **one row and one column**
- use a filter that connects it to the outer row (here, `p.user_id = u.id`)

⚠️ On big tables this can be slow (it re-runs for every row), so test before using it in production.

## Example 2 — subquery in FROM

Find the distribution of customers by number of purchases (e.g. "90 customers made one purchase"):

```sql
SELECT
  purchases,
  count(user_id) AS customers
FROM (SELECT
        user_id,
        count(1) AS purchases
      FROM payments p
      GROUP BY user_id)
GROUP BY purchases
ORDER BY customers DESC;
```

One query wrapped around another — a pattern you'll see constantly.

## Example 3 — subquery in WHERE

Get all purchases made by users named John:

```sql
SELECT *
FROM payments p
WHERE p.user_id IN (
  SELECT u.id
  FROM users u
  WHERE u.first_name = 'John'
);
```

Here the subquery returns **one column but many rows** — perfectly fine when used with `IN` (unlike a SELECT subquery, which must return a single value).

---

> 💡 **Try it:** Find all payments from users in the United States, using a subquery in WHERE.

➡️ Next: **Cleaning up with CTEs (WITH)**
