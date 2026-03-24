# Day 01 — Printing & Output

## Key syntax
```python
print("text")                        # basic
print("a", "b", "c")                 # multiple values, space between
print("a", "b", sep="-")             # custom separator → a-b-c
print("hello", end=" "); print("!") # custom end → hello !
print()                              # blank line

# Escape sequences
"\n"  # newline
"\t"  # tab
"\"" # double quote inside string

# f-strings
name = "Rocket"
f"Hello {name}"          # Hello Rocket
f"Score: {9500:,}"       # Score: 9,500
f"{3.14:.2f}"            # 3.14
```

## Gotchas
- `print` needs parentheses — `print("hi")` not `print "hi"`
- Strings need quotes — `print(hello)` looks for a variable called `hello`
- Single `'` and double `"` quotes both work — be consistent

## Interview tips
- `print()` is for debugging — production code uses `logging`
- `print()` returns `None` — it's a side effect, not a value
- f-strings (Python 3.6+) are faster than `.format()` — prefer them
