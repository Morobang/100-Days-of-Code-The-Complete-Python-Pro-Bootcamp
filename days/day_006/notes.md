# Day 006 — Dictionaries

## Key syntax
```python
d = {"key": "value"}
d["key"]              # access — KeyError if missing
d.get("key")          # None if missing
d.get("key", default) # custom default

d["new"] = val        # add / update
del d["key"]          # delete
d.pop("key", None)    # pop with default

d.keys()              # view of keys
d.values()            # view of values
d.items()             # view of (key, value) pairs

d.update({"x": 1})          # merge in place
{**d1, **d2}                # merge → new dict (d2 wins)
d.setdefault("k", [])       # set only if key absent
```

## Gotchas
- Dict keys must be **hashable** (strings, ints, tuples — not lists)
- Dict preserves **insertion order** (Python 3.7+)
- Iterating and modifying a dict at the same time raises `RuntimeError`

## Interview tips
- "Group items by property" → `setdefault(key, []).append(item)` pattern
- "Find two numbers that sum to target" → store complements in a dict as you go (O(n))
- `collections.Counter` is a dict subclass for frequency counting — mention it
