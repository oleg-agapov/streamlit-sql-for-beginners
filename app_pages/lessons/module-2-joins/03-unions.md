---
title: Stacking Rows with UNION
module: 2 — Joins
order: 3
level: 2
minutes: 5
---

# Stacking Rows with UNION

A **UNION** stacks the results of two or more `SELECT` statements into one table, combining all their rows.

Three rules the queries must follow:

1. same number of columns in each
2. columns in the same order
3. matching data types

These sound strict, but in practice they're just common sense.

## The idea

Imagine two tables, `orders_2020` and `orders_2021`, and you want to analyze both years together:

```sql
SELECT * FROM orders_2020

UNION

SELECT * FROM orders_2021;
```

(Assuming both have identical columns and types.)

## A runnable version on our data

We only have one `payments` table, but we can simulate two sources by filtering by year:

```sql
SELECT event_date, gross_revenue, currency, user_id
FROM payments
WHERE event_date BETWEEN '2020-01-01' AND '2020-12-31 23:59:59'

UNION

SELECT event_date, gross_revenue, currency, user_id
FROM payments
WHERE event_date BETWEEN '2021-01-01' AND '2021-12-31 23:59:59';
```

The result holds rows from both years.

If you add or drop a column on one side, you'll get an error like:

```
SELECTs to the left and right of UNION do not have the same number of result columns
```

## UNION vs UNION ALL

- `UNION` **removes duplicate rows.**
- `UNION ALL` **keeps everything**, including duplicates (and it's faster, since it skips the dedup step).

You can chain as many as you need:

```sql
SELECT * FROM table_1
UNION
SELECT * FROM table_2
UNION
SELECT * FROM table_3;
```

---

> 💡 **Challenge:** Can you rewrite the two-year query above using CTEs?

✅ Next: **Your first JOIN**
