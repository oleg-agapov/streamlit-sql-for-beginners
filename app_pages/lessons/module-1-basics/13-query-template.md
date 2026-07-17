---
title: The Query Template — Putting It All Together
module: 1 — Basics
order: 13
level: 1
minutes: 4
---

# The Query Template — Putting It All Together

By now you've met a lot of clauses, each with its own position. If the ordering feels overwhelming, here's a template to anchor everything.

```sql
SELECT
  /* [Required] one or more columns and aggregations */

FROM
  /* [Required] table name */

WHERE
  /* [Optional] conditions applied to raw rows */

GROUP BY
  /* [Optional] grouping columns, if aggregating */

HAVING
  /* [Optional] conditions on aggregated columns */

ORDER BY
  /* [Optional] sorting columns */

LIMIT
  /* [Optional] number of rows to return */
```

## The order is fixed

You write the clauses in this exact sequence. Only `SELECT` and `FROM` are required; the rest are optional but, when present, must appear in this order.

A useful way to remember the *logical* flow (how the database actually processes it):

1. **FROM** — start with the table
2. **WHERE** — throw away rows that don't match
3. **GROUP BY** — bucket the survivors
4. **HAVING** — throw away buckets that don't match
5. **SELECT** — compute the output columns
6. **ORDER BY** — sort the result
7. **LIMIT** — cut it down to size

Notice that you *write* `SELECT` first but the database *applies* it late. That's why you can use a column in `WHERE` even if you didn't select it — and why an alias defined in `SELECT` isn't always usable in `WHERE`.

---

> 💡 **Keep this template handy.** Every query in the rest of the course is just a variation on it.

✅ **You're through the core mechanics.** Next: transforming columns with functions.
