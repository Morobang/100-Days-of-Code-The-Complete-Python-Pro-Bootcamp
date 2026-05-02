# Day 8 — Quick Reference

## Conversion functions

```python
int("42")       # 42      — string to int
int(3.9)        # 3       — float to int (truncates, does NOT round)
int(True)       # 1
int(False)      # 0

float("3.14")   # 3.14   — string to float
float(42)       # 42.0   — int to float
float("  2.5 ") # 2.5    — strips whitespace

str(100)        # "100"  — int to string
str(3.14)       # "3.14"
str(True)       # "True"

bool(0)         # False
bool("")        # False
bool(None)      # False
bool(1)         # True   — any non-zero / non-empty value
```

## What causes ValueError

```python
int("hello")    # ValueError — not a valid integer
int("3.14")     # ValueError — int() can't parse a decimal string (use float() first)
float("abc")    # ValueError
```

## Safe pattern (for now)

```python
# Convert user input to a number
age = int(input("Enter your age: "))
# If user types something that's not a number, this crashes
# You'll handle that gracefully on Day 54 with try/except
```

## Gotchas

- `int(3.9)` gives `3`, not `4`. It truncates — it does NOT round.
- `int("3.14")` raises a `ValueError`. You cannot convert a decimal string directly to int. Do `int(float("3.14"))` instead.
- `str()` never fails — everything can be converted to a string.
