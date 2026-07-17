---
title: Ranking Functions — ROW_NUMBER, RANK, DENSE_RANK
module: 3 — Window Functions
order: 2
level: 3
minutes: 7
---

# Ranking Functions — ROW_NUMBER, RANK, DENSE_RANK

The three most useful ranking functions are `ROW_NUMBER()`, `RANK()`, and `DENSE_RANK()`.

## ROW_NUMBER()

`ROW_NUMBER()` attaches a sequential number to each row, based on a sort order. Let's number users *within each country*, by registration date:

```sql
SELECT
  id,
  first_name,
  last_name,
  reg_date,
  country,
  ROW_NUMBER() OVER (PARTITION BY country ORDER BY reg_date) AS rn
FROM users;
```

Result:

```
id   | first_name | reg_date            | country     | rn
-----+------------+---------------------+-------------+---
9016 | Andrea     | 2016-05-14 19:47:00 | Afghanistan |  1
6436 | Paul       | 2016-06-22 13:40:48 | Afghanistan |  2
8243 | Michelle   | 2016-07-01 23:31:22 | Afghanistan |  3
3203 | Anthony    | 2016-05-17 16:55:53 | Albania     |  1
7162 | Cynthia    | 2016-06-26 08:36:52 | Albania     |  2
```

What's happening:

1. `ROW_NUMBER()` numbers the rows.
2. `PARTITION BY country` limits the window to each country.
3. `ORDER BY reg_date` decides the numbering order.
4. The counter **resets** at the start of each new partition (notice it restarts at 1 for Albania).

## RANK() vs DENSE_RANK()

These handle **ties** differently:

- `RANK()` — tied rows get the **same** rank, and the next rank is **skipped**. (1, 2, 2, 4…)
- `DENSE_RANK()` — tied rows get the same rank, but the next rank is **not** skipped. (1, 2, 2, 3…)

`ROW_NUMBER()` never ties — every row gets a distinct number even if values are equal.

A quick way to remember:

- Need a unique sequence? → `ROW_NUMBER()`
- Need a leaderboard with gaps after ties? → `RANK()`
- Need a leaderboard without gaps? → `DENSE_RANK()`

---

> 💡 **Try it:** Rank payments from highest to lowest `gross_revenue` using all three functions side by side and compare the output.

➡️ Next: **Aggregating window functions**
