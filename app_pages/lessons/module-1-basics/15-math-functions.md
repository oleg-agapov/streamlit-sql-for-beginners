---
title: Math Functions
module: 1 — Basics
order: 15
level: 1
minutes: 3
---

# Math Functions

**Math functions** apply numeric transformations to your data.

You've already met the aggregation-style math functions:

- `count()`
- `sum()`
- `min()`
- `max()`
- `avg()`

> Remember: those five only apply when **aggregating or grouping** data.

Other useful math functions work row-by-row:

- `round(number, precision)` — round to a given number of decimal places
- `sqrt(number)` — square root
- `power(a, b)` — raise `a` to the power of `b` (both can be numbers or columns)

And the usual operators — `+`, `-`, `*`, `/` — work on numbers and columns alike.

## Example

Calculate net profit (revenue after tax), rounded to 2 decimals:

```sql
SELECT
  round(gross_revenue * (1 - tax_rate), 2) AS net_profit
FROM payments;
```

---

> 💡 **Try it:** Round the average `gross_revenue` to one decimal place.

➡️ Next: **Date functions**
