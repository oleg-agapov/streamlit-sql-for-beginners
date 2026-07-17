---
title: Conditional Functions — coalesce()
module: 1 — Basics
order: 17
level: 1
minutes: 3
---

# Conditional Functions — coalesce()

The last group of column functions is **conditional functions** — they make working with messy data much easier.

`coalesce(arg1, arg2, ...)` takes two or more arguments (columns, strings, numbers) and returns the **first non-NULL** one.

How it works:

- Is the *first* argument NULL? If not, return it. If so, move on.
- Is the *second* argument NULL? If not, return it. If so, move on.
- …and so on.

The classic use is supplying a **default value**. For example, treat a missing revenue as zero:

```sql
SELECT
  coalesce(gross_revenue, 0)
FROM payments;
```

Now NULLs become `0` in the output, which is much friendlier for downstream math and reports.

---

> 💡 **Try it:** Replace any missing `last_name` with the text `'(no surname)'`.

➡️ Next: **The CASE statement**
