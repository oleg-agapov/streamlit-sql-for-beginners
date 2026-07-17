---
title: Why Optimization Matters — Table Scans
module: 5 — The Optimizer
order: 1
level: 5
minutes: 6
---

# Why Optimization Matters — Table Scans

At the top level, you don't just *write* SQL — you write **fast** SQL. A query that works on 1,000 rows can crawl on 100 million. The Optimizer understands not just *what* the database returns, but *how* it gets there.

## What is a table scan?

When you run a query, the database has to find the matching rows. The most basic strategy is a **full table scan**: read *every single row* and check whether it matches.

```sql
SELECT *
FROM users
WHERE email = 'ada@example.com';
```

With no help, the database may inspect all ten million rows just to find the one you want. That's a full table scan — fine for small tables, painful for large ones.

## The mental model: a book with no index

Imagine looking for one topic in a 1,000-page book that has **no index**. You'd flip through every page. That's a table scan.

Now imagine the book *has* an index: you jump to the right page in seconds. That's what a database **index** does (next lesson).

## How to see what the database is doing

Most databases let you inspect the execution plan with `EXPLAIN`:

```sql
EXPLAIN SELECT * FROM users WHERE email = 'ada@example.com';
```

The output (which varies by database) tells you whether it's doing a full scan or using an index. Learning to read `EXPLAIN` output is the single most useful optimization skill — it turns "this query is slow" from a guess into a diagnosis.

## The optimizer's core questions

Whenever performance matters, ask:

- Is this query scanning the whole table when it could target a subset?
- Are the columns I filter and join on indexed?
- Am I moving more data than I need to?

The rest of this module gives you the tools to answer these.

---

➡️ Next: **Indexes — the database's table of contents**
