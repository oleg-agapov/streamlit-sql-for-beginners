---
title: Date Functions
module: 1 — Basics
order: 16
level: 1
minutes: 6
---

# Date Functions

Working with dates is everywhere: daily visitor counts, monthly sales, time-since-signup. SQL provides **date functions** for this.

> ⚠️ Date functions vary *a lot* between databases — names and behavior both differ. Always check your database's documentation.

## SQLite date functions

```sql
/* SQLite */
SELECT
  reg_date                                    -- original value

  , date(reg_date)                            -- truncate to YYYY-MM-DD
  , date('2021-01-01')                        -- parse a string into a date
  , datetime('2021-01-01 23:59:59')           -- keep the time too
  , current_timestamp                         -- right now

  -- modifiers: add/subtract time
  , date('2021-01-01', '+1 day')
  , date('2021-01-01', '-1 month')

  -- difference between two dates in days (can be fractional/negative)
  , julianday(reg_date) - julianday('2021-01-01')
FROM users;
```

## MySQL equivalents

```sql
/* MySQL */
SELECT
  reg_date

  , date(reg_date)
  , date('2021-01-01')
  , timestamp('2021-01-01 23:59:59')
  , current_timestamp

  -- add/subtract with INTERVAL
  , reg_date + INTERVAL 1 DAY   AS next_day
  , reg_date - INTERVAL 1 MONTH AS month_ago

  -- whole-day difference
  , datediff('2021-01-01', reg_date)
FROM users;
```

Some functions match between databases; others don't. The docs are your friend.

## Dates as strings

In many databases a date written as a string (e.g. `'2021-01-01 00:00:00'`) is interpreted as a date automatically, so you can filter without explicit conversion:

```sql
SELECT *
FROM users
WHERE reg_date BETWEEN '2021-01-01 00:00:00' AND '2021-01-31 23:59:59';
```

Some databases require an explicit date function — again, check your docs.

---

> 💡 **Try it:** List users who registered in January 2019.

➡️ Next: **Conditional logic — coalesce and CASE**
