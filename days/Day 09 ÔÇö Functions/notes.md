# Day 09 — Functions

## Key syntax
```python
def fn(a, b=default):
    """Docstring."""
    return result

# Multiple returns
def minmax(lst): return min(lst), max(lst)
lo, hi = minmax([3,1,4])

# Scope — LEGB: Local → Enclosing → Global → Built-in
```

## Gotchas
- No `return` → function returns `None`
- Default mutable arg: `def fn(lst=[])` is a bug — use `None`
- Variables defined inside a function are LOCAL — invisible outside

## Interview tips
- One function, one job — keep them small
- Name as verbs: `calculate_bmi`, `is_valid`, `get_user`
- Docstrings are good practice — `help(fn)` reads them
