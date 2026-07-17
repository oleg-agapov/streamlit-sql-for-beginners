---
title: Filtering Groups with HAVING
module: 1 — Basics
order: 12
level: 1
minutes: 4
---

# Filtering Groups with HAVING

There's one more thing you'll want from grouping: filtering by the **aggregated value** itself.

Say you want users with a *unique* first name. The steps:

1. group `users` by `first_name`
2. count how many users share each name
3. keep only names that appear exactly once

Your instinct might be to put the count in `WHERE`. But that fails — **`WHERE` can only filter raw columns, not aggregated values.**

The fix is `HAVING`:

```sql
SELECT
  first_name,
  count(id) AS count_users
FROM users
GROUP BY first_name
HAVING count_users > 1;
```

`HAVING` always goes **after** `GROUP BY`. Like `WHERE`, it can hold multiple conditions.

## WHERE vs HAVING — the key distinction

- **`WHERE`** filters individual rows *before* grouping.
- **`HAVING`** filters groups *after* aggregation.

A query can use both:

```sql
SELECT country, count(id) AS users
FROM users
WHERE email LIKE '%@gmail.com'   -- filter rows first
GROUP BY country
HAVING users > 100;              -- then filter groups
```

---

> 💡 **Try it:** Find first names shared by more than one user.

✅ **You've finished grouping.** Next: a mental model for the whole query.
