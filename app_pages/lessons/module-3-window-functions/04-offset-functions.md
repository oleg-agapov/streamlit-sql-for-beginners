---
title: Offset Functions — LAG and LEAD
module: 3 — Window Functions
order: 4
level: 3
minutes: 5
---

# Offset Functions — LAG and LEAD

Sometimes you need to look at a *neighboring* row from the current one — the previous value or the next value. That's what offset functions do:

- `LAG()` — reach **back** to a previous row
- `LEAD()` — reach **forward** to a next row

Order matters for these, so always include `ORDER BY` in the window.

```sql
SELECT
  id,
  reg_date,
  country,
  LAG(id)  OVER (ORDER BY reg_date) AS previous_user_id,
  LEAD(id) OVER (PARTITION BY country ORDER BY reg_date) AS next_user_from_country
FROM users;
```

- `previous_user_id` — the `id` of the user who registered just before this one (globally, by date)
- `next_user_from_country` — the `id` of the next user to register *in the same country*

## Offsets and defaults

Both functions accept extra arguments to skip more than one row and to set a fallback when no neighbor exists (otherwise you get `NULL`):

```sql
LAG(column_name, offset, default_value) OVER (...)
```

- `offset` — how many rows back/forward (default 1)
- `default_value` — what to return when there's no such row

## Why this is powerful

`LAG`/`LEAD` make "compared to last period" calculations trivial — month-over-month growth, day-over-day change, time between events. For example, current revenue minus `LAG(revenue)` gives you the change from the prior row, no self-join required.

---

> 💡 **Try it:** For monthly revenue, add a column showing the previous month's revenue using `LAG`, then compute the difference.

✅ **You've finished Module 3 — Window Functions.** You now know the techniques behind ~95% of daily SQL work.
