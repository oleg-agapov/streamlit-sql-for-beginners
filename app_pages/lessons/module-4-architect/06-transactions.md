---
title: Transactions — All or Nothing (COMMIT & ROLLBACK)
module: 4 — The Architect
order: 6
level: 4
minutes: 6
---

# Transactions — All or Nothing (COMMIT & ROLLBACK)

When you start *changing* data — inserts, updates, deletes — you need a safety net. What if a multi-step change half-succeeds and then crashes? **Transactions** solve this.

**A transaction groups several statements into a single unit that either fully succeeds or fully fails — never halfway.**

The classic example is a bank transfer: subtract money from account A, add it to account B. If the first step runs but the second fails, money vanishes. A transaction guarantees both happen, or neither does.

## The commands

```sql
BEGIN;                       -- start a transaction

UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;

COMMIT;                      -- make all changes permanent
```

- **`BEGIN`** (or `START TRANSACTION`) — open a transaction
- **`COMMIT`** — save everything done since `BEGIN`, permanently
- **`ROLLBACK`** — undo everything since `BEGIN`, as if it never happened

If something looks wrong before you commit:

```sql
BEGIN;
DELETE FROM payments WHERE gross_revenue < 0;
-- wait, that deleted more than expected...
ROLLBACK;   -- nothing was actually deleted
```

## ACID — the guarantees

Transactions are the backbone of what databases call **ACID** guarantees:

- **Atomicity** — all steps happen, or none do
- **Consistency** — the database moves from one valid state to another
- **Isolation** — concurrent transactions don't trip over each other
- **Durability** — once committed, changes survive crashes

You don't need to memorize ACID, but the takeaway is simple: transactions are how databases stay trustworthy under failure and concurrency.

## A practical habit

When you're about to run a risky `UPDATE` or `DELETE`, wrap it in a transaction. Run it, check the result with a `SELECT`, and only then `COMMIT`. If it looks wrong, `ROLLBACK`. This habit has saved countless people from costly mistakes.

> Note: support and default behavior vary. Some tools auto-commit each statement unless you explicitly `BEGIN`. Know your environment.

---

✅ **You've finished Module 4 — The Architect.** You can now build and safely change a database, not just read from it. Next: making it fast.
