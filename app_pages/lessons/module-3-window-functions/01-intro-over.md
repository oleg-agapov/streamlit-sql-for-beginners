---
title: Why Window Functions Exist
module: 3 — Window Functions
order: 1
level: 3
minutes: 6
---

# Why Window Functions Exist

You've calculated lots of aggregates with `GROUP BY` — monthly revenue, users per country, and so on. But `GROUP BY` has a side effect: it **collapses rows**. Group by country and you get one row per country; the individual users disappear.

Sometimes you want the aggregate *alongside* the original rows, without losing them. That's the job of **window functions**.

**A window function performs a calculation over a subset of rows ("a window") and returns a value in a new column — without reducing the number of rows.**

## The OVER syntax

Window functions use a special form:

```sql
function_name([parameters])
OVER (
    [PARTITION BY column_set]
    [ORDER BY column_set]
    [frame_clause]
)
```

It looks heavy, but you rarely use all of it at once:

1. **function name** (with optional parameters) — what to calculate
2. **OVER** — required; marks this as a window function
3. **PARTITION BY** — split the data into groups; the function runs within each. *Optional.*
4. **ORDER BY** — sort rows within the window (needed for running totals, rankings, etc). *Optional.*
5. **frame clause** — fine-grained control over which rows are in the window. *Optional, advanced.*

## Three families of window functions

- **Ranking functions** — assign a rank or row number
- **Aggregating functions** — `sum`, `count`, `avg`… computed over a window
- **Offset functions** — peek at neighboring rows (previous/next)

The next three lessons take each in turn.

---

> 💡 **Key mental shift:** `GROUP BY` *replaces* rows with summaries. Window functions *add a column* and keep every row.

➡️ Next: **Ranking functions**
