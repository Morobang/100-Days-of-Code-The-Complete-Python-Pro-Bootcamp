# Day 11 — Dictionaries

## Key syntax
```python
d = {"key": "value"}
d["key"]              # KeyError if missing
d.get("key")          # None if missing
d.get("key", default)
d["new"] = val
del d["key"]
d.pop("key", None)
d.keys()  d.values()  d.items()
"key" in d
d.update({"x":1})
{**d1, **d2}          # merge (d2 wins)

# Dict comprehension
{k: v for k, v in items if condition}
```

## Gotchas
- Keys must be hashable — strings/ints/tuples yes, lists no
- Dict preserves insertion order (Python 3.7+)
- Iterating and modifying at the same time → RuntimeError

## Interview tips
- Frequency counter: `freq[x] = freq.get(x, 0) + 1`
- "Two Sum" → store complements in a dict as you scan — O(n)
- `collections.Counter` is a dict built for counting
