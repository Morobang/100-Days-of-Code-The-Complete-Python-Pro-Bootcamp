# Day 12 — Tuples & Sets

## Tuples
```python
t = (1, 2, 3)
t[0]              # access
a, b, c = t       # unpack
first, *rest = t  # starred unpack
(42,)             # single-item tuple — trailing comma required!
```

## Sets
```python
s = {1, 2, 3}
s = set()         # empty set — NOT {} (that's a dict!)
s.add(x)
s.discard(x)      # no error if missing
s.remove(x)       # KeyError if missing

a | b   # union
a & b   # intersection
a - b   # difference
a ^ b   # symmetric difference
a <= b  # is a a subset of b?
```

## Gotchas
- `(42)` is NOT a tuple — `(42,)` is
- Sets are unordered — no indexing
- `set()` for empty, not `{}` (that's an empty dict)
- `in` is O(1) for sets, O(n) for lists

## Interview tips
- "Find duplicates" → `len(lst) != len(set(lst))`
- "Common elements" → set intersection `a & b`
- Tuple as dict key → `grid[(x, y)] = value` pattern
