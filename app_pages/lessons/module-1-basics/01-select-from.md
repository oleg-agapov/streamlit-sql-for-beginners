---
title: Your First Query — SELECT and FROM
module: 1 — Basics
order: 1
level: 1
minutes: 4
---

# Your First Query — SELECT and FROM

Let's write the simplest possible query. This returns every record from a table called `users`:

```sql
SELECT *
FROM users;
```

Here's what each piece means:

1. `SELECT` — a required keyword telling the database you want to retrieve data.
2. `*` — a wildcard meaning "all columns."
3. `FROM` — another keyword saying *which* table to read.
4. `users` — the table name.
5. `;` — marks the end of the statement. (For a single statement, you can often omit it.)

In plain English: *"select all columns from the `users` table and return them to me."* It's like opening a spreadsheet and seeing everything at once.

## A few syntax rules worth knowing early

1. **Keywords are reserved words.** You generally can't use them as table or column names. No need to memorize them all — just be aware.
2. **Case doesn't matter for keywords.** `SELECT` and `select` both work. A good habit: keywords in UPPERCASE, table and column names in lowercase.
3. **Statements end with `;`.** This means you can spread a query across many lines or cram it onto one:
   ```sql
   SELECT * FROM users;
   ```
4. **Order matters.** `SELECT` is required and comes first; `FROM` follows. You can't write `FROM` before `SELECT`.

---

> 💡 **Try it:** Run `SELECT * FROM users;` against the sample database and look at what comes back.

➡️ Next: **Picking columns and limiting rows**
