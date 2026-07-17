---
title: Combining Conditions — AND, OR, NOT
module: 1 — Basics
order: 4
level: 1
minutes: 6
---

# Combining Conditions — AND, OR, NOT

One condition is rarely enough. Want all the Johns from the United States? Combine conditions with the **logical operators** `AND`, `OR`, and `NOT`.

## AND — both must be true

```sql
-- all Johns from the United States
SELECT id, first_name, country
FROM users
WHERE first_name = 'John' AND country = 'United States';
```

## OR — at least one must be true

```sql
-- everyone named John (any country)
-- plus everyone from the US (any name)
SELECT id, first_name, last_name, country
FROM users
WHERE first_name = 'John' OR country = 'United States'
LIMIT 5;
```

## NOT — flip the condition

```sql
SELECT id, email
FROM users
WHERE NOT email LIKE '%@bing.com';

-- cleaner: put NOT right before LIKE
SELECT id, email
FROM users
WHERE email NOT LIKE '%@bing.com';
```

`NOT` also works with `IN` (`email NOT IN (...)`), but **not** with `=`, `!=`, or the inequality operators.

## Precedence: AND beats OR

When you chain conditions, which runs first?

```sql
SELECT *
FROM users
WHERE id >= 500
  AND email LIKE '%bing.com'
  OR country IN ('United States', 'Canada');
```

In SQL, **`AND` has higher priority than `OR`** — just as multiplication beats addition in math. So this:

```sql
WHERE
  first_name = 'John'
  OR
  first_name = 'Bella' AND country = 'Brazil'
```

means: *all Johns from any country*, **plus** *Bellas, but only from Brazil*.

## Use brackets to stay sane

If precedence is hard to track, use parentheses — the highest priority, just like in math:

```sql
WHERE
  first_name = 'John'
  OR
  (first_name = 'Bella' AND country = 'Brazil');
```

Same result, far easier to read.

---

> 💡 **Try it:** Find users from Canada whose email is *not* on gmail.

➡️ Next: **Handling missing data with NULL**
