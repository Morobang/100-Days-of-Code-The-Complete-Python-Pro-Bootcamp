# Day 04 — User Input & Type Casting

## Key syntax
```python
name = input("Prompt: ")        # always returns str
age  = int(input("Age: "))      # convert immediately
price = float(input("Price: ")) # float for decimals

# Integer division and remainder
17 // 5    # → 3  (how many times 5 fits in 17)
17 % 5     # → 2  (what's left over)

# Useful for converting seconds → h/m/s
total = 3661
hours   = total // 3600
minutes = (total % 3600) // 60
seconds = total % 60
```

## Gotchas
- `input()` ALWAYS returns a string — convert before doing math
- `int("3.14")` raises ValueError — use `float()` first then `int()` if needed
- `int(input(...))` will crash if the user types something that isn't a number — handle with try/except (Day 09)

## Interview tips
- `//` is floor division — rounds down: `7 // 2 == 3`
- `%` is modulo — gives the remainder: `7 % 2 == 1`
- These two operators come up constantly in interview problems
