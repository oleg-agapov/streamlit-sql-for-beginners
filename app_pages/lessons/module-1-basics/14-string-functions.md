---
title: String Functions
module: 1 — Basics
order: 14
level: 1
minutes: 5
---

# String Functions

Often you need to *transform* data into a new shape: join a first and last name into a full name, extract part of a date, recalculate a price. SQL has **column functions** for this.

Crucially: **column functions don't change the stored data.** The transformation only affects your result set — the source table is safe.

> Function names vary between databases. When something doesn't work, check your database's docs for the equivalent.

Here are the most common **string functions**:

```sql
SELECT
  /* lower() → lowercase */
  lower(first_name) AS lower_name,

  /* upper() → UPPERCASE */
  upper(last_name) AS upper_surname,

  /* || concatenates strings/columns */
  /* MySQL alternative: concat() */
  first_name || ' ' || last_name AS full_name,

  /* length() → length of the string */
  /* MySQL alternative: len() */
  length(email) AS length_of_email
FROM users;
```

## Handy patterns

**Lowercasing to compare reliably** — users enter names inconsistently ("John", "JOHN", "JoHn"):

```sql
SELECT count(first_name)
FROM users
WHERE lower(first_name) = 'john';
```

**Nesting functions:**

```sql
SELECT
  length(lower(first_name) || ' ' || lower(last_name)) AS full_name_length
FROM users;
```

**Functions inside grouping** — find users with a unique full name:

```sql
SELECT
  first_name || ' ' || last_name AS full_name,
  count(id) AS count_users
FROM users
GROUP BY first_name || ' ' || last_name
HAVING count_users = 1;
```

---

> 💡 **Try it:** Build a `full_name` column and return it for the first 10 users.

➡️ Next: **Math functions**
