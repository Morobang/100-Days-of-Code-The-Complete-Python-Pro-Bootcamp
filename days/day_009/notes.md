# Day 009 — Functions: Basics & Scope

## Key syntax
```python
def fn(a, b=10):     # b has default value
    return a + b

# Multiple returns (returns a tuple)
def minmax(lst):
    return min(lst), max(lst)

lo, hi = minmax([3,1,4])

# Scope rules — LEGB
# Local → Enclosing → Global → Built-in
x = 'global'
def outer():
    x = 'enclosing'
    def inner():
        x = 'local'   # only visible inside inner
        return x
```

## Gotchas
- Default mutable arguments are evaluated ONCE: `def fn(lst=[])` is a bug
- `global x` inside a function lets you modify the global — avoid this pattern
- Functions are first-class objects — they can be passed as arguments and returned

## Interview tips
- Closure = inner function that remembers enclosing scope after outer has returned
- "Make a counter" → standard closure interview question
- Know the difference between `return` and `yield` — yield makes a generator
