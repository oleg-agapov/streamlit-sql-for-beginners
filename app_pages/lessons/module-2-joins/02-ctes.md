---
title: Cleaning Up with CTEs (WITH)
module: 2 — Joins
order: 2
level: 2
minutes: 5
---

# Cleaning Up with CTEs (WITH)

Nested subqueries get hard to read fast. **Common Table Expressions** (CTEs) fix that by letting you name a sub-result and refer to it by that name.

The shape:

```sql
WITH table_expression_name AS (
    query_definition
)
-- you can define more, separated by commas

SELECT *
FROM table_expression_name;
```

How it works:

- `WITH` declares a temporary, named table.
- You give it any name you like.
- You define it with a `SELECT`.
- You can chain several CTEs.
- Then a normal `SELECT` references them.

## Refactoring a subquery into a CTE

Remember the purchase-distribution query with a subquery in FROM? Here's the same logic as a CTE:

```sql
WITH table_purchases AS (
    SELECT
        user_id,
        count(1) AS purchases
    FROM payments p
    GROUP BY user_id
)

SELECT
    purchases,
    count(user_id) AS customers
FROM table_purchases
GROUP BY purchases
ORDER BY customers DESC;
```

Now there are two clear parts:

- `table_purchases` computes purchases per user
- the outer `SELECT` builds the distribution on top of it

Same result, far easier to read — and you can build queries step by step. CTEs are one of the best habits you can pick up early.

---

> 💡 **Try it:** Rewrite Example 2 from the subqueries lesson as a CTE (you basically just did).

✅ Next: **Stacking rows with UNION**
