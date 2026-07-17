---
title: Sorting Results with ORDER BY
module: 1 — Basics
order: 11
level: 1
minutes: 5
---

# Sorting Results with ORDER BY

To make output readable, sort it with `ORDER BY`. You can sort by columns *or* by aggregates.

```sql
-- alphabetical by country
SELECT
  country,
  count(id) AS count_users
FROM users
GROUP BY country
ORDER BY country;

-- by user count, ascending
SELECT
  country,
  count(id) AS count_users
FROM users
GROUP BY country
ORDER BY count_users;

-- top 10 countries by users (DESC + LIMIT)
SELECT
  country,
  count(id) AS count_users
FROM users
GROUP BY country
ORDER BY count_users DESC
LIMIT 10;
```

`DESC` flips the order to descending. (`ASC` is the default and rarely written.)

## Things to know about ORDER BY

- It works **without** `GROUP BY` too — handy for listing rows sorted by a column.
- With grouping, `ORDER BY` goes **after** `GROUP BY`.
- You can sort by an alias, or repeat the aggregation function directly:
  ```sql
  ORDER BY count(id)
  ```
- You can sort by multiple columns:
  ```sql
  ORDER BY first_name
         , last_name
         , country DESC
  ```

---

> 💡 **Try it:** List the top 5 countries by number of users.

➡️ Next: **Filtering groups with HAVING**
