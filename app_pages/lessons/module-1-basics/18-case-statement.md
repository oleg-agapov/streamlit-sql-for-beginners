---
title: The CASE Statement
module: 1 — Basics
order: 18
level: 1
minutes: 6
---

# The CASE Statement

`CASE` is a conditional function that checks one or more conditions and returns a value based on which one matches. Think of it as SQL's if/else.

Basic syntax:

```sql
case
  when /* condition 1 */          -- required
    then /* value if condition 1 is true */
  when /* condition 2 */          -- optional
    then /* value if condition 2 is true */
  /* more when branches as needed */
  else                            -- optional
    /* value if nothing matched */
end
```

Looks dense, but it gets natural fast.

## Example 1 — the simplest CASE

Return `'It is John'` when the first name is John, otherwise NULL:

```sql
SELECT
  case
    when first_name = 'John' then 'It is John'
  end AS is_john
FROM users;
```

Combine it with grouping to count Johns vs everyone else:

```sql
SELECT
  case
    when first_name = 'John' then 'It is John'
  end AS is_john,
  count(1)
FROM users
GROUP BY is_john;
```

## Example 2 — adding ELSE

Return `'It is not John'` instead of NULL:

```sql
SELECT
  case
    when first_name = 'John' then 'It is John'
    else 'It is not John'
  end AS is_john
FROM users;
```

## Example 3 — multiple conditions

Bucket users by when they registered — this year, last year, or earlier:

```sql
SELECT
  case
    -- registered this year?
    when strftime('%Y', reg_date) = strftime('%Y', current_timestamp)
      then 'Registered this year'

    -- registered last year? (subtract 1 year from today)
    when strftime('%Y', reg_date) = strftime('%Y', date(current_timestamp, '-1 year'))
      then 'Registered last year'

    -- otherwise
    else 'Registered more than two years ago'
  end AS registration_period,
  count(1)
FROM users
GROUP BY registration_period;
```

> ⚠️ `CASE` is evaluated **top to bottom**. As soon as one condition matches, it returns that `then` value and stops checking the rest. Order your conditions accordingly.

---

> 💡 **Try it:** Label payments as `'big'` when `gross_revenue >= 90`, else `'small'`, and count each.

✅ **You've finished Module 1 — the Basics.** This is the foundation everything else builds on.
