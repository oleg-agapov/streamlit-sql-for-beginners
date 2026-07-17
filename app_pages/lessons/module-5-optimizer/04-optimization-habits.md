---
title: Writing Optimized SQL — Habits and What's Next
module: 5 — The Optimizer
order: 4
level: 5
minutes: 6
---

# Writing Optimized SQL — Habits and What's Next

Indexes and partitions are tools. But most everyday speed-ups come from a handful of habits in how you *write* queries. Here are the ones with the biggest payoff.

## Practical optimization habits

1. **Select only the columns you need.** `SELECT *` drags every column across the wire. Name the columns you actually use.
2. **Filter as early and as specifically as possible.** A tight `WHERE` clause shrinks the working set before any heavy work happens.
3. **Filter on indexed/partitioned columns** when you can — that's what lets the database prune and seek instead of scan.
4. **Mind the join grain.** Duplicated rows (from the Joins module) silently inflate aggregates *and* waste work. Know how many rows each join can produce.
5. **Aggregate before joining** when it reduces row counts. Joining two small summaries beats joining two huge raw tables.
6. **Avoid per-row subqueries on big tables.** A correlated subquery in `SELECT` runs once per row — a join or window function is usually far cheaper.
7. **Read the plan.** `EXPLAIN` turns "feels slow" into "here's the full scan." Always confirm your change actually helped.

## A simple loop to live by

> Measure → find the bottleneck → make one change → measure again.

Optimization without measurement is superstition. Change one thing at a time and let `EXPLAIN` and the clock tell you if it worked.

---

# Where to go from here

You now have the SQL that covers the large majority of real-world data work — selecting, filtering, aggregating, joining, windowing, building structures, and making it all fast.

There's always more depth to explore when you need it:

- **Advanced DDL** — managing tables, schemas, and constraints in detail.
- **Advanced grouping and filtering** — `CUBE`, `ROLLUP`, and `QUALIFY` (check your database's support).
- **Procedural extensions and deeper transaction control** — stored procedures and database-specific languages.
- **Security** — access rights, roles, and protecting sensitive data.

A couple of places to keep learning:

- [awesome-database-learning](https://github.com/pingcap/awesome-database-learning)
- [awesome-tech: databases](https://awesome-tech.readthedocs.io/databases/)

The best next step, though, is to keep writing queries against real data. Every function here has hidden corners you'll discover only by using it.

✅ **Congratulations — you've completed all five levels of SQL.** Happy querying.
