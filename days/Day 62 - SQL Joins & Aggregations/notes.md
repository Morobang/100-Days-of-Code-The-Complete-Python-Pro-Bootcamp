# Day 62 — SQL Joins & Aggregations

## JOIN types
```sql
INNER JOIN   -- only matching rows in both
LEFT JOIN    -- all from left + matching right (NULL if no match)
```

## GROUP BY + HAVING
```sql
SELECT col, COUNT(*), SUM(val), AVG(val)
FROM t
WHERE condition           -- filter BEFORE grouping
GROUP BY col
HAVING COUNT(*) > 5       -- filter AFTER grouping
ORDER BY SUM(val) DESC
LIMIT 10
```

## Subqueries
```sql
-- scalar
SELECT name FROM customers
WHERE id = (SELECT customer_id FROM orders ORDER BY total DESC LIMIT 1)

-- NOT IN for "never ordered"
SELECT name FROM products
WHERE id NOT IN (SELECT DISTINCT product_id FROM order_items)

-- LEFT JOIN alternative for "never ordered"
SELECT p.name FROM products p
LEFT JOIN order_items oi ON p.id=oi.product_id
WHERE oi.id IS NULL
```

## Interview tips
- `WHERE` before `GROUP BY`, `HAVING` after — know the order
- "Never ordered" → LEFT JOIN + IS NULL or NOT IN subquery
- Window functions: `ROW_NUMBER() OVER (ORDER BY col DESC)`
