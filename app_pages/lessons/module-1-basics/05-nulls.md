---
title: Handling Missing Data with NULL
module: 1 — Basics
order: 5
level: 1
minutes: 4
---

# Handling Missing Data with NULL

Sometimes a value is simply missing — a customer skipped their last name, or a delivery date isn't known yet. SQL represents "no value" with `NULL`.

`NULL` means **the value does not exist**. It is *not* the same as an empty string `''` or zero `0`. Think of it as a placeholder for "not provided."

## Checking for NULL

You can't test for `NULL` with `=`. Use the `IS` operator instead:

```sql
-- users who skipped the last_name field
SELECT first_name, last_name
FROM users
WHERE last_name IS NULL;
```

## Checking for "not NULL"

```sql
SELECT first_name, last_name
FROM users
WHERE last_name IS NOT NULL;
```

> ⚠️ A common beginner mistake: `WHERE last_name = NULL` does **not** work the way you expect. Always use `IS NULL` / `IS NOT NULL`.

`NULL` will come up again — in aggregations (which often skip it) and in joins (where unmatched rows produce NULLs). Keep this mental model: *NULL = unknown / absent.*

---

> 💡 **Try it:** Count is for later, but for now just list users who *do* have a last name.

✅ **You've finished the filtering basics.** Next: aggregations.
