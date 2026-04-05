# Day 005 — Tuples & Sets

## Tuples
```python
t = (1, 2, 3)
a, b, c = t           # unpacking
first, *rest = t      # starred unpacking → rest = [2, 3]
x, y = y, x           # swap — uses tuple packing/unpacking

t.count(1)            # 1
t.index(2)            # 1
len(t)                # 3
```

## Sets
```python
s = {1, 2, 3}
s.add(4)
s.discard(99)         # no error if missing
s.remove(99)          # KeyError if missing

a | b    # union
a & b    # intersection
a - b    # difference (in a, not in b)
a ^ b    # symmetric difference (in one but not both)
a <= b   # is a a subset of b?
```

## Gotchas
- Tuples are immutable — use them for data that shouldn't change (coordinates, DB rows)
- `(1)` is NOT a tuple — `(1,)` is
- Sets are unordered — never index them
- Set elements must be hashable — no lists inside sets

## Interview tips
- "Find common elements of two arrays" → convert to sets, use `&` → O(n)
- "Find duplicates" → compare `len(lst)` vs `len(set(lst))`
- Tuple as dict key: coordinates `(x, y)` as keys is a common pattern
