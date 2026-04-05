# Day 61 — SQL Basics with Python

## Key syntax
```python
import sqlite3

conn = sqlite3.connect('file.db')   # file
conn = sqlite3.connect(':memory:')  # in-memory
conn.row_factory = sqlite3.Row      # rows as dicts

cur = conn.cursor()
cur.execute('SQL', (params,))        # ALWAYS use params
cur.executemany('SQL', [(r1),(r2)])
cur.fetchone(); cur.fetchall()
conn.commit(); conn.rollback()
conn.close()
```

## SQL quick reference
```sql
CREATE TABLE t (id INTEGER PRIMARY KEY, name TEXT, price REAL)
INSERT INTO t (name,price) VALUES (?,?)
SELECT * FROM t WHERE genre=? ORDER BY price DESC LIMIT 10
UPDATE t SET price=? WHERE id=?
DELETE FROM t WHERE id=?
SELECT genre, COUNT(*), AVG(price) FROM t GROUP BY genre
```

## Gotchas
- NEVER use f-strings for SQL values — SQL injection!
- Always use `?` placeholders for values
- `conn.commit()` required for INSERT/UPDATE/DELETE
- `with sqlite3.connect() as conn:` auto-commits

## Interview tips
- Know the difference between `fetchone()` and `fetchall()`
- `row_factory = sqlite3.Row` makes rows dict-like
- Parameterised queries prevent SQL injection — always use them
