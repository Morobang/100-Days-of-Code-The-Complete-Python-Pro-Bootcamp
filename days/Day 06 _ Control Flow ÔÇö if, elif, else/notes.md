# Day 06 — Control Flow: if / elif / else

## Key syntax
```python
if x > 0:
    print("positive")
elif x < 0:
    print("negative")
else:
    print("zero")

# Ternary (one-liner)
label = "even" if x % 2 == 0 else "odd"

# Comparison
==  !=  >  <  >=  <=

# Logical
and   or   not

# Membership
x in [1, 2, 3]
x not in [1, 2, 3]
```

## Gotchas
- `=` assigns, `==` compares — very common mistake
- `elif` stops at the FIRST True condition — order matters
- Indentation is not optional in Python — it defines the block

## Interview tips
- Leap year is a classic condition question — know the rule cold
- "Replace if-elif with a dict" is a common refactor ask
- FizzBuzz: check `% 15` FIRST (both conditions), then `% 3`, then `% 5`
