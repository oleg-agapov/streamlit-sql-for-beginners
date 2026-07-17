---
title: sum, min, max, avg — and Math on Columns
module: 1 — Basics
order: 7
level: 1
minutes: 5
---

# sum, min, max, avg — and Math on Columns

Beyond `count()`, four aggregation functions cover most numeric needs:

- `sum()` — total of a column
- `min()` — smallest value
- `max()` — largest value
- `avg()` — average

Using the `payments` table:

```sql
SELECT
  sum(gross_revenue),  -- total revenue
  min(gross_revenue),  -- smallest payment
  max(gross_revenue),  -- largest payment
  avg(gross_revenue)   -- average payment
FROM payments;
```

> ⚠️ Some databases mishandle NULLs in aggregations. If you `sum()` a column containing NULLs, you may get NULL back. Be aware of your data.

## Math on aggregations

You can combine aggregations with arithmetic. A classic business metric — **Average Revenue Per User** — is total revenue divided by the number of unique users:

```sql
SELECT
  sum(gross_revenue) / count(distinct user_id)
FROM payments;
```

## Math on raw columns

Arithmetic also works row-by-row on non-aggregated columns (this is applied to each row individually):

```sql
SELECT
  gross_revenue * tax_rate - 0.30
FROM payments;
```

The usual operators `+`, `-`, `*`, `/` all work, on both numbers and columns.

---

> 💡 **Try it:** What's the total `gross_revenue` across all payments?

➡️ Next: **Naming your output with aliases**
