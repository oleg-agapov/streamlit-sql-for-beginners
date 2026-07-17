---
title: Views — Saving a Query for Reuse
module: 4 — The Architect
order: 5
level: 4
minutes: 6
---

# Views — Saving a Query for Reuse

A **view** is a virtual table. It doesn't store data itself — it stores a *query*, and runs it whenever you select from it. Views are how you give a complex query a friendly, reusable name.

How views work:

1. You write a `SELECT` that returns some result set.
2. You wrap it in a view, giving that result set a name.
3. Next time you need that data, you query the view instead of rewriting the SQL.

## Example — a monthly tax report

**Task:** every month you owe taxes, and you need the amount per month.

The underlying query:

```sql
SELECT
  strftime('%Y-%m', event_date) AS report_month,
  round(sum(gross_revenue * tax_rate), 2) AS tax_amount
FROM payments
GROUP BY 1
ORDER BY 1;
```

Result:

```
report_month | tax_amount
-------------+-----------
2018-05      |     234.16
2018-06      |     453.14
2018-07      |     319.35
```

You have two options: save the SQL somewhere and paste it each time, or turn it into a view. Let's make a view:

```sql
CREATE VIEW tax_view AS
SELECT
  strftime('%Y-%m', event_date) AS report_month,
  round(sum(gross_revenue * tax_rate), 2) AS tax_amount
FROM payments
GROUP BY 1
ORDER BY 1;
```

Now query it like any table:

```sql
SELECT * FROM tax_view;
```

Same result — but you never have to remember the query again. No data is stored; the view is just a live reflection of `payments`.

## Materialized views

Some databases offer **materialized views**, which *do* store a physical copy of the result. They're faster to read (the work is already done) but can go stale and need refreshing. Plain views are always current but recompute on every query. Pick based on whether you value freshness or speed.

## Why views matter to the Architect

Views let you:

- hide complexity behind a simple name
- present a clean, consistent interface to analysts
- restrict what data people see (expose a view, not the raw table)

---

> 💡 **Try it:** Create a view `monthly_revenue` that returns total `gross_revenue` per month, then select from it.

➡️ Next: **Transactions — all or nothing**
