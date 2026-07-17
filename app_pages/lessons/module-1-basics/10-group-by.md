---
title: Grouping with GROUP BY
module: 1 — Basics
order: 10
level: 1
minutes: 6
---

# Grouping with GROUP BY

`count()` tells you how many users you have. But what if you want the breakdown — *how many users per country*?

You could write a filtered count for each country one at a time, but with hundreds of countries that's hopeless. Instead, use **grouping**.

**Grouping lets you run aggregations over groups of rows.**

```sql
SELECT
  country,
  count(id) AS count_users
FROM users
GROUP BY country;
```

Step by step:

1. In `SELECT` you list two kinds of things:
   - the **grouping column(s)** — here, `country`
   - the **aggregation(s)** — here, `count(id)`
2. Add `GROUP BY` at the bottom with the columns you're grouping over (`country`).

The result has one row per country, with its user count.

You can group by more than one column (just add them to `GROUP BY`) and include as many aggregations as you like.

## Grouping with filters

You can mix `GROUP BY` and `WHERE`. Count gmail users per country:

```sql
SELECT
  country,
  count(id) AS gmail_users
FROM users
WHERE email LIKE '%@gmail.com'
GROUP BY country;
```

`WHERE` filters the rows *first*, then grouping and counting happen on what remains.

## Clause order matters

A reliable order to memorize:

1. `SELECT` — always first
2. `FROM`
3. `WHERE` — after `FROM`
4. `GROUP BY` — after `WHERE`

---

> 💡 **Try it:** Count payments per `currency`.

➡️ Next: **Sorting results with ORDER BY**
