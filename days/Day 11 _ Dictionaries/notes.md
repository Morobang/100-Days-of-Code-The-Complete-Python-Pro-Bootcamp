# Day 11 — Dictionaries

## Key syntax
```python
d = {"key": "value", "num": 42}

d["key"]              # access — KeyError if missing
d.get("key")          # None if missing
d.get("key", default) # custom default

d["new"] = val        # add / update
del d["key"]          # delete
d.pop("key", None)    # delete with default (no error)

d.keys()              # all keys
d.values()            # all values
d.items()             # (key, value) pairs

"key" in d            # membership check
len(d)                # number of keys

d.update({"x": 1})         # merge another dict in
{**d1, **d2}               # merge two dicts → new dict
d.setdefault("k", [])      # set only if key not already there
```

## Gotchas
- Keys must be **hashable** — strings, ints, tuples work. Lists do not
- Dicts preserve **insertion order** (Python 3.7+)
- `d["missing"]` raises KeyError — use `.get()` when unsure

## Interview tips
- "Count frequency of items" → build a freq dict with `.get(k, 0) + 1`
- "Two sum" problem → store complements in a dict as you go — O(n) solution
- `collections.Counter` is a dict subclass built for counting — worth knowing
