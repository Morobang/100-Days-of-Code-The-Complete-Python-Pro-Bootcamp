# Day 02 — Variables & Data Types

## Key syntax
```python
name = "Rocket"       # str
age = 23              # int
height = 1.75         # float
active = True         # bool

type(name)            # → <class 'str'>

# Type conversion
int("42")             # → 42
float("3.14")         # → 3.14
str(99)               # → "99"
bool(0)               # → False  (0, "", [], None are all falsy)
bool("False")         # → True   (any non-empty string is truthy!)
```

## Gotchas
- `bool("False")` is `True` — any non-empty string is truthy
- `int(3.9)` → `3` — it truncates, doesn't round
- Variable names are case-sensitive: `Name` and `name` are different
- Can't start a variable name with a number: `1name` is invalid

## Interview tips
- Python is **dynamically typed** — types are checked at runtime, not compile time
- Python is **strongly typed** — `"3" + 3` raises a TypeError (unlike JavaScript)
- Know your falsy values: `0`, `0.0`, `""`, `[]`, `{}`, `None`, `False`
