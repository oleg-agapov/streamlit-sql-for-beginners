---
title: Naming Your Output with Aliases
module: 1 — Basics
order: 8
level: 1
minutes: 4
---

# Naming Your Output with Aliases

After applying a function, the output column name looks ugly — something like `sum(gross_revenue) / count(distinct user_id)`. **Aliases** fix that by renaming the column.

Use the `AS` keyword:

```sql
SELECT
  sum(gross_revenue) / count(distinct user_id) AS avg_revenue_per_user
FROM payments;
```

Much nicer to read.

## Aliases with spaces

Aliases can't contain spaces or start with a number — unless you wrap them in double quotes:

```sql
SELECT
  sum(gross_revenue) / count(distinct user_id) AS "Avg Revenue per User"
FROM payments;
```

> You can alias **any** column, not just aggregated ones.

## Aliasing tables

You can also alias tables and refer to columns through that short name:

```sql
SELECT
  u.id,     -- column "id" via the table alias
  u.email
FROM users AS u;   -- alias "users" as "u"
```

Table aliases feel pointless now, but they become essential once you start joining tables — typing `users.country` over and over gets old fast.

---

> 💡 **Try it:** Rename `count(*)` on the `users` table to `total_users`.

➡️ Next: **Aggregating filtered data**
