---
title: Indexes — The Database's Table of Contents
module: 5 — The Optimizer
order: 2
level: 5
minutes: 7
---

# Indexes — The Database's Table of Contents

An **index** is a separate data structure the database keeps so it can find rows *without* scanning the whole table. Like the index at the back of a book, it maps values to locations — so a lookup becomes a jump instead of a search.

## Creating an index

```sql
CREATE INDEX idx_users_email ON users (email);
```

Now a query filtering on `email` can use the index to jump straight to matching rows instead of scanning every one:

```sql
SELECT * FROM users WHERE email = 'ada@example.com';  -- now fast
```

You can index multiple columns together (a **composite index**), which helps queries that filter on those columns in order:

```sql
CREATE INDEX idx_users_country_reg ON users (country, reg_date);
```

## When indexes help most

- columns in `WHERE` filters
- columns used in `JOIN ... ON` conditions
- columns in `ORDER BY`
- foreign keys (very common to index these)

Primary keys are indexed automatically — that's part of why joining on `id` is fast.

## Indexes aren't free

This is the key trade-off the Optimizer must respect:

- **Reads get faster**, sometimes dramatically.
- **Writes get slower** — every `INSERT`, `UPDATE`, and `DELETE` must also update the index.
- **Indexes take storage** — they're extra data structures on disk.

So you don't index everything. You index the columns your *actual queries* filter and join on. An unused index is pure cost.

## A practical workflow

1. Find a slow query.
2. Run `EXPLAIN` to confirm it's doing a full scan.
3. Add an index on the filtered/joined column.
4. Re-run `EXPLAIN` to confirm the index is now used.
5. Verify the query is actually faster.

> 💡 Don't guess. Measure first, index second, measure again. Adding indexes blindly can hurt as often as it helps.

---

➡️ Next: **Partitioning — dividing big tables**
