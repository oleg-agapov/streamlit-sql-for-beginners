---
title: Thinking in Tables, Rows, and Columns
module: 0 — Getting Started
order: 3
level: 0
minutes: 4
---

# Thinking in Tables, Rows, and Columns

On a basic level, working with SQL feels a lot like working in Excel.

Imagine a big spreadsheet of users for some service. You can already do plenty with that data:

- inspect it — check which columns exist and what values they hold
- count the rows
- find a specific user by name
- filter to see how many users come from a particular country

SQL does all of this — and much more.

## A bit of database vocabulary

A few terms will make the rest of the course easier to follow.

- **Table** — the database equivalent of a spreadsheet. A table holds data of one kind (for example, only users). It has a fixed set of **columns** (also called *fields*) and an unlimited number of **rows** (also called *records*).
- **Column** — every value in one column shares a single data type (string, number, date, and so on).
- **Row** — one record: a single unit of data, like everything known about one user.
- **Schema** — a way to group related tables. A `store` schema might hold `customers`, `shipments`, and `products`. Schemas keep tables logically organized.

A database can hold many tables; schemas help you keep them tidy.

## The two tables you'll use

Throughout this course, examples reference two tables.

**`users`** — people registered on an imaginary online store:

```
id | first_name | last_name | email                         | reg_date            | country
---+------------+-----------+-------------------------------+---------------------+--------------------
 1 | Danielle   | Johnson   | danielle.johnson88@gmail.com  | 2018-04-08 03:47:32 | Burundi
 2 | Jill       |           | jill.rhodes07@gmail.com       | 2019-12-16 12:45:52 | Antigua and Barbuda
 3 | Anthony    | Robinson  | anthony.robinson04@hotmail.com| 2016-08-05 02:39:30 | Moldova
```

**`payments`** — purchases those users made:

```
id | event_date          | gross_revenue | currency | user_id | tax_rate
---+---------------------+---------------+----------+---------+---------
 1 | 2021-02-01 11:04:21 |         99.99 | EUR      |     861 |     0.18
 2 | 2018-11-04 02:14:12 |         99.99 | EUR      |    5735 |     0.32
 3 | 2018-06-22 23:58:55 |         99.99 | USD      |    4427 |     0.18
```

Notice that `payments.user_id` points back to `users.id`. That link is what makes joins possible later on.

---

✅ **You've finished Module 0.** Next up: writing your first query.
