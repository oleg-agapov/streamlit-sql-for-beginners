---
title: Aggregating Filtered Data
module: 1 — Basics
order: 9
level: 1
minutes: 4
---

# Aggregating Filtered Data

Aggregating the *whole* table is the exception, not the rule. Most of the time you want an aggregate over a *filtered* subset — and you already know the tool for that: `WHERE`.

Count the Johns from the United States:

```sql
SELECT
  count(id)
FROM users
WHERE country = 'United States'
  AND first_name = 'John';
```

The `WHERE` clause runs first, narrowing the rows; then `count()` aggregates what's left.

## Math never changes your source data

A quick but important reassurance: transforming a column in `SELECT` does **not** alter the stored data. For example:

```sql
SELECT
  gross_revenue * (1 + 0.2) AS gross_revenue
FROM payments;
```

This bumps `gross_revenue` by 20% *in the output only*. The underlying table is untouched. You can prove it by showing both side by side:

```sql
SELECT
  gross_revenue AS source_gross_revenue,
  gross_revenue * (1 + 0.2) AS gross_revenue
FROM payments;
```

The original column is right there, unchanged.

---

> 💡 **Try it:** What's the average `gross_revenue` for payments made in `USD`?

✅ **You've finished basic aggregations.** Next: grouping.
