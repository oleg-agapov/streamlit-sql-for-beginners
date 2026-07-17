---
title: ALTER and DROP — Changing Structure
module: 4 — The Architect
order: 4
level: 4
minutes: 5
---

# ALTER and DROP — Changing Structure

Tables aren't carved in stone. As requirements change, you'll need to modify or remove them. Two commands handle this: `ALTER` (change) and `DROP` (delete).

## ALTER TABLE — modify an existing table

Add a column:

```sql
ALTER TABLE users ADD COLUMN phone VARCHAR(20);
```

Rename a column (syntax varies by database):

```sql
ALTER TABLE users RENAME COLUMN phone TO phone_number;
```

Remove a column:

```sql
ALTER TABLE users DROP COLUMN phone_number;
```

> Different databases support different `ALTER` operations. SQLite, for instance, historically had limited `ALTER` support and sometimes required rebuilding the table. Check your database's docs.

## DROP — delete a table or view

`DROP TABLE` removes a table **and all its data**, permanently:

```sql
DROP TABLE payments;
```

There's no undo. To avoid an error if the table might not exist:

```sql
DROP TABLE IF EXISTS payments;
```

## DROP vs DELETE vs TRUNCATE

These are easy to confuse:

- **`DELETE FROM table`** — removes *rows* (you can filter with `WHERE`); the table structure stays.
- **`TRUNCATE table`** — removes *all rows* fast; structure stays. (Not in every database.)
- **`DROP TABLE`** — removes the *entire table*, structure included.

```sql
DELETE FROM payments WHERE gross_revenue = 0;  -- just some rows
TRUNCATE TABLE payments;                        -- all rows, keep table
DROP TABLE payments;                            -- gone entirely
```

> ⚠️ `DROP` and `TRUNCATE` are blunt instruments and usually can't be rolled back as easily as `DELETE`. Double-check before running them — especially in production.

---

> 💡 **Try it:** Add a `notes` column to your `products` table, then drop it again.

➡️ Next: **Views — saving a query for reuse**
