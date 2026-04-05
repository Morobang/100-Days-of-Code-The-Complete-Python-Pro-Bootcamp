# Day 03 — String Manipulation

## Key syntax
```python
# Concatenation
"Hello" + " " + "World"      # → "Hello World"

# f-strings (preferred)
f"Name: {name}, Age: {age}"
f"Result: {2 + 2}"           # can do expressions
f"{price:.2f}"               # format to 2 decimal places

# Common methods
s.upper()        # ALL CAPS
s.lower()        # all lowercase
s.strip()        # remove whitespace from both ends
s.lstrip()       # remove from left only
s.rstrip()       # remove from right only
s.replace(a, b)  # replace all occurrences of a with b
s.split(",")     # split into list on delimiter
s.startswith("x")
s.endswith("x")
s.count("x")     # count occurrences
len(s)           # length

# Slicing
s[0]      # first char
s[-1]     # last char
s[1:4]    # chars at index 1, 2, 3
s[::-1]   # reversed
```

## Gotchas
- Strings are **immutable** — methods return a NEW string, they don't modify in place
- `"hello".upper()` works but `s = "hello"; s[0] = "H"` raises a TypeError
- `" ".join(words)` is faster than concatenating with `+` in a loop

## Interview tips
- Reverse a string → `s[::-1]` (O(n), idiomatic Python)
- Check palindrome → `s == s[::-1]`
- f-strings are faster than `.format()` — prefer them
