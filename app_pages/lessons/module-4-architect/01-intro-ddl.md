---
title: From Querying to Building — DDL
module: 4 — The Architect
order: 1
level: 4
minutes: 6
---

# From Querying to Building — DDL

Everything so far has been about *reading and reshaping* data that already exists. But at some point you need to **create the structure** itself — the tables your data lives in. That's the Architect's job.

This is **DDL — Data Definition Language**: the part of SQL that defines and changes the shape of your database, rather than the data inside it.

The three core DDL commands are `CREATE`, `ALTER`, and `DROP`. We'll meet them across the next few lessons. First, the building blocks: data types.

## Why data types matter

Every column has a **type**, and the type is a contract: it controls what values are allowed, how they're stored, how they sort, and which functions apply. Put a date in a proper date column and date math just works; store it as plain text and you'll fight it forever.

## Common data types

Exact names vary by database, but these families show up everywhere:

| Family | Typical names | Use for |
|---|---|---|
| Integer | `INTEGER`, `INT`, `BIGINT` | whole numbers, IDs, counts |
| Decimal | `DECIMAL(p,s)`, `NUMERIC`, `REAL`, `FLOAT` | money, measurements |
| Text | `VARCHAR(n)`, `TEXT`, `CHAR(n)` | names, emails, descriptions |
| Date/Time | `DATE`, `TIMESTAMP`, `DATETIME` | events, registrations |
| Boolean | `BOOLEAN`, `BOOL` | true/false flags |

> 💡 For money, prefer `DECIMAL`/`NUMERIC` over floating-point types. Floats can introduce tiny rounding errors that are unacceptable in financial data.

## A note on database dialects

SQLite is famously loose about types (it uses "type affinity" and won't stop you putting text in a number column). Databases like PostgreSQL and Snowflake are strict. When you move from learning to production, expect types to be enforced more rigorously — that strictness is a feature, not a nuisance.

---

➡️ Next: **CREATE TABLE — defining structure**
