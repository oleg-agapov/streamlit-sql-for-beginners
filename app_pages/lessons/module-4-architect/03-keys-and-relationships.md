---
title: Relationships — Primary and Foreign Keys
module: 4 — The Architect
order: 3
level: 4
minutes: 6
---

# Relationships — Primary and Foreign Keys

Back in the Joins module, you joined `payments` to `users` on `payments.user_id = users.id`. That link wasn't an accident — it's a **relationship**, and keys are what make it official.

## Primary key

A **primary key** uniquely identifies each row in a table. In `users`, that's `id`. Properties:

- unique across the whole table
- never NULL
- ideally stable (it shouldn't change over a row's lifetime)

This is why `users.id` is a safe thing to join on: there's exactly one user per `id`.

## Foreign key

A **foreign key** is a column that points to the primary key of another table. In `payments`, `user_id` is a foreign key referencing `users.id`:

```sql
CREATE TABLE payments (
  id            INTEGER       PRIMARY KEY,
  event_date    TIMESTAMP     NOT NULL,
  gross_revenue DECIMAL(10,2) NOT NULL,
  currency      VARCHAR(3),
  user_id       INTEGER       NOT NULL,
  tax_rate      DECIMAL(4,2),
  FOREIGN KEY (user_id) REFERENCES users(id)
);
```

The `FOREIGN KEY ... REFERENCES` line tells the database that every `user_id` in `payments` must correspond to a real `id` in `users`. This is called **referential integrity** — the database will reject a payment for a user that doesn't exist.

## How keys relate to joins

This is the payoff of the whole "relational" idea:

- **primary key** → the unique identity of a row
- **foreign key** → a reference to a row in another table
- **join** → the query that follows that reference to combine the tables

When you write `JOIN users ON users.id = payments.user_id`, you're walking the foreign-key relationship from a payment back to its user.

> 💡 Well-designed keys make joins obvious and prevent whole classes of data bugs. When you design a table, ask: *what uniquely identifies a row here, and which other tables does it point to?*

---

➡️ Next: **ALTER and DROP — changing structure**
