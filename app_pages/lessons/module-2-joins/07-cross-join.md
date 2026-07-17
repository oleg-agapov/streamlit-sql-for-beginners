---
title: CROSS JOIN and Self-Joins
module: 2 — Joins
order: 7
level: 2
minutes: 6
---

# CROSS JOIN and Self-Joins

A **cross join** pairs *every* row of the left table with *every* row of the right table. It's also called the **Cartesian product**.

Because it matches everything with everything, a cross join needs **no key** (though you can still filter afterward with `WHERE`).

## A small illustration

Two tiny tables:

```
col1        col2
----        ----
   1        bar
   2        baz
   3        foo
```

Cross join them by listing both in `FROM`, separated by a comma:

```sql
SELECT *
FROM table_1, table_2;
```

Output — all 9 combinations:

```
col1 | col2
-----+-----
   1 | bar
   1 | baz
   1 | foo
   2 | bar
   2 | baz
   2 | foo
   3 | bar
   3 | baz
   3 | foo
```

## A real use: rolling totals (self-join)

Cross joins shine for **recursive-style** calculations. Here's a running monthly revenue total — each month sums itself plus all earlier months:

```sql
WITH table_monthly_sales AS (
    SELECT
        strftime('%Y-%m', event_date) AS report_month,
        sum(gross_revenue) AS gross_revenue
    FROM payments
    GROUP BY 1
)
SELECT
    t1.report_month,
    t1.gross_revenue,
    sum(t2.gross_revenue) AS rolling_gross_revenue
FROM table_monthly_sales t1, table_monthly_sales t2
WHERE t2.report_month <= t1.report_month
GROUP BY 1, 2;
```

The table is cross-joined **with itself** (a *self-join*). The `WHERE t2.report_month <= t1.report_month` keeps, for each month `t1`, every month up to and including it — then `sum()` adds them up.

Take your time with this one; it's a clever pattern that gets easier with practice.

## When to use which join — recap

- **INNER** — rows matching in both tables
- **LEFT** — all left rows, plus matches where they exist
- **CROSS** — every combination of rows
- **Self-join** — joining a table to itself for advanced calculations
- Joins can use **multiple keys**, not just one column

---

> 💡 **Try it:** Build the rolling revenue query above and read the output month by month.

✅ **You've finished Module 2 — Joins.** Next level: window functions.
