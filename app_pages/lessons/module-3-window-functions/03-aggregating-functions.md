---
title: Aggregating Window Functions
module: 3 — Window Functions
order: 3
level: 3
minutes: 7
---

# Aggregating Window Functions

You can use familiar aggregates — `SUM`, `COUNT`, `AVG`, `MIN`, `MAX` — as window functions. They calculate a value within the window, **without collapsing rows**. If you leave out `PARTITION BY`, they behave as a **running** aggregation.

## Running total

Calculate a running monthly revenue total:

```sql
WITH table_monthly_sales AS (
    SELECT
        strftime('%Y-%m', event_date) AS report_month,
        sum(gross_revenue) AS gross_revenue
    FROM payments
    GROUP BY 1
)
SELECT
    report_month,
    gross_revenue,
    sum(gross_revenue) OVER (ORDER BY report_month) AS rolling_gross_revenue
FROM table_monthly_sales;
```

Compare this to the cross-join version from the Joins module — the window function does the same job far more elegantly. The `ORDER BY` inside `OVER` is what makes it *running*: each row sums itself and everything before it.

## Resetting each year with PARTITION BY

Want the running total to restart every year? Add `PARTITION BY report_year`:

```sql
WITH table_monthly_sales AS (
    SELECT
        strftime('%Y-%m', event_date) AS report_month,
        strftime('%Y', event_date) AS report_year,
        sum(gross_revenue) AS gross_revenue
    FROM payments
    GROUP BY 1
)
SELECT
    report_month,
    gross_revenue,
    sum(gross_revenue) OVER (PARTITION BY report_year ORDER BY report_month) AS rolling_gross_revenue
FROM table_monthly_sales;
```

## Share of total (PARTITION BY without ORDER BY)

To find each month's contribution to its year, first compute the yearly total, then divide:

```sql
WITH table_monthly_sales AS (
    SELECT
        strftime('%Y-%m', event_date) AS report_month,
        strftime('%Y', event_date) AS report_year,
        sum(gross_revenue) AS gross_revenue
    FROM payments
    GROUP BY 1
)
SELECT
    report_month,
    gross_revenue,
    sum(gross_revenue) OVER (PARTITION BY report_year) AS total_yearly_amount,
    gross_revenue / sum(gross_revenue) OVER (PARTITION BY report_year) AS contribution
FROM table_monthly_sales;
```

Notice: here `SUM` uses `PARTITION BY` **without** `ORDER BY`. That gives the *full* partition total on every row (not a running one) — exactly what you need for a share-of-total calculation.

> 🔑 The presence or absence of `ORDER BY` inside `OVER` is the difference between a **running** total and a **whole-partition** total.

---

> 💡 **Try it:** Add a column showing each month's running total *and* its share of the yearly total in one query.

➡️ Next: **Offset functions — LAG and LEAD**
