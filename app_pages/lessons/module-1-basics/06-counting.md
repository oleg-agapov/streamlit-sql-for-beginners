---
title: Counting Rows
module: 1 — Basics
order: 6
level: 1
minutes: 5
---

# Counting Rows

So far you've pulled raw rows. But often you don't want the rows themselves — you want a **statistic** about them: how many rows, the average value, the total. That's what **aggregation functions** are for.

The simplest one counts rows:

```sql
SELECT count(*)
FROM users;
```

This returns the number of rows in `users`. Aggregation functions go right after `SELECT`.

## count(*) vs count(column)

The `*` means "count all rows." If you pass a **column name** instead, it counts only the rows where that column is **not NULL**:

```sql
SELECT count(id)
FROM users;
```

Since `id` rarely contains NULLs, this usually matches `count(*)`. But `count(last_name)` would skip users with no last name.

## Multiple counts at once

```sql
SELECT
  count(*),
  count(last_name)
FROM users;
```

The gap between these two numbers tells you how many users are missing a last name.

## Counting distinct values

Add `distinct` to count unique values:

```sql
SELECT count(distinct first_name)
FROM users;
```

This returns how many *unique* first names exist.

> ⚠️ Both `count(column)` and `count(distinct column)` **ignore NULL values**. `count(*)` does not.

---

> 💡 **Try it:** How many distinct countries are represented in the `users` table?

➡️ Next: **sum, min, max, avg**
