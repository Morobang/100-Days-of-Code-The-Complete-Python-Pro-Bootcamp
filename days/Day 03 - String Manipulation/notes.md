# Day 03 — String Manipulation

## Key syntax
```python
s.upper()         s.lower()         s.strip()
s.lstrip()        s.rstrip()        s.replace(a, b)
s.split()         s.split(",")      " ".join(lst)
s.startswith("x") s.endswith("x")  s.count("x")
s.find("x")       s.index("x")     len(s)

# Slicing
s[0]      # first char
s[-1]     # last char
s[1:4]    # index 1,2,3
s[::-1]   # reversed
s[::2]    # every 2nd

# f-string format specs
f"{val:.2f}"    # 2 decimal places
f"{val:,}"      # comma separator
f"{val:.1%}"    # percentage
f"{val:>10}"    # right-align width 10
f"{val:<10}"    # left-align
```

## Gotchas
- Strings are **immutable** — methods return NEW strings
- `s.split()` with no arg splits on any whitespace + removes empties
- `"hello"[100:]` doesn't crash — returns `""` (slicing never raises IndexError)

## Interview tips
- Reverse → `s[::-1]` (O(n), idiomatic)
- Palindrome → `s.lower() == s.lower()[::-1]`
- f-strings are faster than `.format()` — always prefer them
