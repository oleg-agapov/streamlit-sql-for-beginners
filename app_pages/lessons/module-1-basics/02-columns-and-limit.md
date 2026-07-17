---
title: Picking Columns and Limiting Rows
module: 1 — Basics
order: 2
level: 1
minutes: 4
---

# Picking Columns and Limiting Rows

Real tables can be huge — millions or billions of rows. So `SELECT *` has a "bad smell": ask for everything and you might get buried.

## LIMIT — cap the number of rows

Add a `LIMIT` clause to return only the first few rows:

```sql
SELECT *
FROM users
LIMIT 10;
```

This gives you the first 10 records.

> `LIMIT` should always be the **very last** clause in a query, or you'll get an error.

## Selecting specific columns

Instead of `*`, list the columns you actually want, separated by commas:

```sql
SELECT first_name, last_name, country
FROM users
LIMIT 10;
```

Now you get just those three columns, and only 10 rows.

## A static column

Sometimes you want a column with a fixed value for every row. SQL lets you do that easily:

```sql
SELECT
  'static column'
  , id
  , first_name
FROM users
LIMIT 10;
```

Every row gets the literal text `static column` in the first column.

---

> 💡 **Try it:** Return just `email` and `country` for the first 5 users.

➡️ Next: **Filtering with WHERE**
