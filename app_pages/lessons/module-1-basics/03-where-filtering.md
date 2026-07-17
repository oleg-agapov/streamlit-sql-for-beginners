---
title: Filtering with WHERE
module: 1 — Basics
order: 3
level: 1
minutes: 6
---

# Filtering with WHERE

To keep only the rows you care about, use `WHERE`. It always goes **after** `FROM`:

```sql
SELECT first_name, last_name, country
FROM users
WHERE country = 'China'
LIMIT 10;
```

After `WHERE` comes a **condition**. Here it's:

```sql
country = 'China'
```

You can put a condition on any column — and you're not limited to checking equality.

## Common comparison operators

| Condition | What it does | Example |
|---|---|---|
| `>`, `>=`, `<`, `<=` | Inequality — great for numbers and dates | `WHERE id >= 2` |
| `!=` | Not equal — everything *except* a value | `WHERE name != 'John'` |
| `IN (...)` | Value is in a set (any data type) | `WHERE country IN ('France', 'Germany')` |
| `LIKE 'pattern'` | Match strings/substrings; `%` is a wildcard for any number of characters | `WHERE email LIKE '%@gmail.com'` |
| `BETWEEN x AND y` | A range; both ends included | `WHERE event_date BETWEEN '2021-01-01' AND '2021-01-01 23:59:59'` |

A couple of examples:

```sql
-- the LIKE operator: all yahoo.com addresses
SELECT *
FROM users
WHERE email LIKE '%@yahoo.com';

-- the IN operator: users from France or Germany
SELECT *
FROM users
WHERE country IN ('France', 'Germany');
```

## Bonus: comments

You may have spotted new syntax above — comments:

```sql
-- this is a single-line comment

/*
this is a multi-line comment.
it can span several lines
*/
```

Comments are ignored by the database. Use them to explain your intent.

---

> 💡 **Try it:** Find all users whose email ends in `@gmail.com`.

➡️ Next: **Combining conditions with AND, OR, NOT**
