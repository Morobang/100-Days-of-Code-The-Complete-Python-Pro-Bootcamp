# Day 01 — Printing & Output

## Key syntax
```python
print("Hello")                        # basic print
print("Hello", "World")               # multiple values — space between
print("a", "b", "c", sep="-")        # custom separator → a-b-c
print("Hello", end=" "); print("!")   # custom end → Hello !
print()                               # prints a blank line
```

## Gotchas
- `print` is a **function** — always needs parentheses: `print()` not `print`
- Strings must be wrapped in quotes — `print(hello)` looks for a variable called `hello`
- Single `'` and double `"` quotes both work — just be consistent

## Interview tips
- `print()` is for debugging — in production code you use logging
- Know that `print()` returns `None` — it's a side effect, not a value
