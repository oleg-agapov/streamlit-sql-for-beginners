---
title: Partitioning — Dividing Big Tables
module: 5 — The Optimizer
order: 3
level: 5
minutes: 6
---

# Partitioning — Dividing Big Tables

When a table grows enormous — billions of rows — even good indexes have limits. **Partitioning** physically splits one big table into smaller pieces (partitions) based on a column's value, while you still query it as a single table.

## The idea

Suppose `payments` holds ten years of data, but most queries only ask about a single month or year. If the table is **partitioned by date**, a query for January 2021 can read *only* the January 2021 partition and skip the rest entirely. This is called **partition pruning** — the database eliminates whole chunks of data before it even starts scanning.

```sql
SELECT sum(gross_revenue)
FROM payments
WHERE event_date BETWEEN '2021-01-01' AND '2021-01-31';
-- with date partitioning, only the relevant partition(s) are read
```

## Common partitioning strategies

- **Range partitioning** — by a range of values, most often dates (one partition per month or year). The most common in analytics.
- **List partitioning** — by a discrete set of values (e.g. one partition per region).
- **Hash partitioning** — by a hash of a column, to spread data evenly across partitions.

## Partitioning vs indexing

They solve related but different problems:

- An **index** helps you find *specific rows* quickly within a table.
- **Partitioning** helps you *skip entire sections* of data you don't need.

They work together: a partitioned table can also have indexes within each partition.

## A modern note

Partitioning is central to cloud data warehouses like **BigQuery** and **Snowflake**, where you partition (and often *cluster*) large tables so queries scan less data — which directly reduces both runtime and cost, since these systems often bill by data scanned. The principle is the same everywhere: **the cheapest data to process is data you never read.**

> ⚠️ Syntax for partitioning varies widely between databases, and lightweight ones like SQLite don't support it natively. The concept, though, is universal and worth understanding before you reach for it.

---

➡️ Next: **Writing optimized SQL — practical habits**
