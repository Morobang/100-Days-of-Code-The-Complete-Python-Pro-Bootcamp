# Day 21 — Recursion

## Key syntax
```python
def fn(n):
    if n == base: return base_val   # base case — MUST have one
    return fn(smaller_n)            # recursive call

# Memoize
from functools import lru_cache
@lru_cache(maxsize=None)
def fib(n): ...
```

## Classic patterns
```python
# Factorial
def factorial(n): return 1 if n==0 else n*factorial(n-1)

# Sum of list
def rsum(lst): return 0 if not lst else lst[0]+rsum(lst[1:])

# Deep flatten
def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list): result.extend(flatten(item))
        else: result.append(item)
    return result
```

## Gotchas
- Missing base case = infinite recursion = RecursionError
- Python default limit is 1000 frames
- Naive recursion is often O(2^n) — memoize overlapping subproblems

## Interview tips
- Every recursive solution has an iterative equivalent — know both
- "Can you do it without recursion?" is a common follow-up
- Tree traversal, directory walking, JSON parsing = natural recursion fits
