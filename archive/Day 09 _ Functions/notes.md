# Day 09 — Functions

## Key syntax
```python
def function_name(param1, param2, default_param=value):
    """Optional docstring describing what this does."""
    # body
    return result

# Call it
result = function_name(arg1, arg2)

# Multiple return values (returns a tuple)
def minmax(lst):
    return min(lst), max(lst)

lo, hi = minmax([3, 1, 4])
```

## Gotchas
- A function without `return` returns `None`
- Default mutable args are a bug: `def fn(lst=[])` — use `None` as default instead
- Variables defined inside a function are local — invisible outside

## Interview tips
- Keep functions small and focused — one function, one job
- Name functions as verbs: `calculate_bmi`, `is_valid`, `get_user`
- Adding a docstring is good practice and shows maturity
