# Day 001 — String Basics

## Key syntax
```python
s[0]        # first char
s[-1]       # last char
s[1:3]      # slice: index 1 up to (not including) 3
s[::-1]     # reverse — step of -1 walks backwards
s.lower()   # lowercase copy
s.upper()   # uppercase copy
len(s)      # length
"el" in s   # membership check → True/False
```

## Gotchas
- Strings are **immutable** — you can't do `s[0] = 'X'`
- `s[1:3]` gives chars at index 1 and 2, **not** 3
- `s[::-1]` is idiomatic Python for reversing — learn it, use it
- `.lower()` returns a **new** string, it doesn't modify in place

## Interview tips
- "Reverse a string" → always answer with slicing `[::-1]`, mention it's O(n)
- Palindrome questions often follow up with "what about spaces/punctuation?" — be ready to strip and normalise
- Know `ord(char)` and `chr(code)` — comes up in Caesar cipher / encoding questions
