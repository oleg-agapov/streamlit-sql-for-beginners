---
title: Keeping Unmatched Rows — LEFT and RIGHT JOIN
module: 2 — Joins
order: 5
level: 2
minutes: 6
---

# Keeping Unmatched Rows — LEFT and RIGHT JOIN

Inner join only keeps matches. But sometimes you want *all* rows from one table even when there's no match in the other.

**Task:** list every user and their lifetime spending. If a user never bought anything, leave the spending empty.

The trap: if you inner-join `users` to `payments`, users with zero purchases vanish (they match nothing in `payments`). The fix is a **LEFT JOIN**:

```sql
SELECT
  first_name,
  last_name,
  sum(gross_revenue) AS total_spendings
FROM users
LEFT JOIN payments ON payments.user_id = users.id
GROUP BY first_name, last_name
ORDER BY total_spendings DESC;
```

## How LEFT JOIN behaves

- where keys match → you get the joined data
- where the right table has no match → you get **NULLs** for its columns
- **no rows are dropped from the main (left) table**

So every user appears, and the ones who never paid simply show NULL spending.

## RIGHT JOIN

`RIGHT JOIN` is the mirror image: it keeps every row from the **joined (right)** table and drops unmatched rows from the main table. In practice, most people just flip the table order and use `LEFT JOIN` — it's easier to reason about — but it's good to know `RIGHT JOIN` exists.

## Quick mental model

- **INNER** → only rows in *both*
- **LEFT** → all rows from the *left*, matched data where it exists
- **RIGHT** → all rows from the *right*, matched data where it exists

---

> 💡 **Try it:** List all users and how many payments each made — including users with zero.

➡️ Next: **A trap — row duplication in joins**
