# Day 12 — Tuples & Sets

## Tuples
```python
t = (1, 2, 3)
t[0]              # access by index
len(t)            # length
a, b, c = t       # unpacking
first, *rest = t  # starred unpacking

# One-element tuple needs a trailing comma
single = (42,)    # NOT (42) — that's just 42
```

## Sets
```python
s = {1, 2, 3}
s = set()             # empty set — NOT {} (that's a dict!)
s.add(4)
s.discard(99)         # no error if missing
s.remove(99)          # KeyError if missing

a | b    # union
a & b    # intersection
a - b    # difference
a ^ b    # symmetric difference
a <= b   # is a a subset of b?
```

## Gotchas
- Tuples are immutable — `t[0] = 99` raises TypeError
- `(42)` is NOT a tuple — `(42,)` is
- Sets are unordered — no indexing, no slicing
- `set()` for empty set, not `{}` (that creates an empty dict)
- `in` is O(1) for sets, O(n) for lists — use sets for membership checks

## Interview tips
- "Find duplicates in a list" → `len(lst) != len(set(lst))`
- "Find common elements" → set intersection `a & b`
- Tuple as dict key — useful for 2D grid coordinates: `grid[(x, y)] = value`
