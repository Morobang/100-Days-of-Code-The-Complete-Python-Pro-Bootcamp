# Day 02 — Variables & Data Types

## Key syntax
```python
name = "Rocket"       # str
age  = 23             # int
gpa  = 3.8            # float
pro  = True           # bool

type(name)            # → <class 'str'>

# Type conversion
int("42")             # → 42
float("3.14")         # → 3.14
str(99)               # → "99"
bool(0)               # → False
bool("False")         # → True  ← surprise! non-empty string is truthy

# Multiple assignment
x, y = 1, 2
a, b = b, a           # swap (no temp variable needed)
```

## Gotchas
- `bool("False")` is `True` — any non-empty string is truthy
- `int(3.9)` → `3` — truncates, doesn't round
- Variables are **case-sensitive**: `Name` ≠ `name`
- Can't start with a digit: `1name` is invalid

## Interview tips
- Python is **dynamically typed** — types checked at runtime, not compile time
- Python is **strongly typed** — `"3" + 3` raises TypeError (unlike JavaScript)
- Falsy values: `0`, `0.0`, `""`, `[]`, `{}`, `None`, `False`
