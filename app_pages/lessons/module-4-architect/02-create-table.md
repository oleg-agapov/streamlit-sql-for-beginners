---
title: CREATE TABLE — Defining Structure
module: 4 — The Architect
order: 2
level: 4
minutes: 7
---

# CREATE TABLE — Defining Structure

`CREATE TABLE` defines a new table: its name, its columns, each column's type, and the rules those columns must obey.

Here's how the `users` table you've been querying might be defined:

```sql
CREATE TABLE users (
  id          INTEGER      PRIMARY KEY,
  first_name  VARCHAR(100) NOT NULL,
  last_name   VARCHAR(100),
  email       VARCHAR(255) NOT NULL UNIQUE,
  reg_date    TIMESTAMP    DEFAULT current_timestamp,
  country     VARCHAR(100)
);
```

Reading it line by line:

- `id INTEGER PRIMARY KEY` — a whole number that uniquely identifies each row (more below)
- `first_name VARCHAR(100) NOT NULL` — text up to 100 chars; **cannot** be empty
- `last_name VARCHAR(100)` — text, and *allowed* to be NULL
- `email ... NOT NULL UNIQUE` — required, and no two rows may share the same value
- `reg_date TIMESTAMP DEFAULT current_timestamp` — if not provided, defaults to "now"
- `country VARCHAR(100)` — optional text

## Constraints — the rules

Constraints are how a table protects its own integrity:

- **`PRIMARY KEY`** — uniquely identifies each row; implies `NOT NULL` and `UNIQUE`. Every table should have one.
- **`NOT NULL`** — the column must always have a value.
- **`UNIQUE`** — no duplicate values allowed.
- **`DEFAULT value`** — used when no value is supplied on insert.
- **`FOREIGN KEY`** — links a column to another table's key (next lesson).

## Putting data in

Once the table exists, add rows with `INSERT`:

```sql
INSERT INTO users (first_name, last_name, email, country)
VALUES ('Ada', 'Lovelace', 'ada@example.com', 'United Kingdom');
```

You can insert several rows at once:

```sql
INSERT INTO users (first_name, email, country)
VALUES
  ('Grace', 'grace@example.com', 'United States'),
  ('Alan',  'alan@example.com',  'United Kingdom');
```

(Notice `last_name` was omitted — allowed, because it isn't `NOT NULL`.)

---

> 💡 **Try it:** Create a small `products` table with an `id`, a `name`, and a `price`, then insert two rows.

➡️ Next: **Relationships and foreign keys**
