# Day 04 — User Input & Type Casting

## Key syntax
```python
name  = input("Prompt: ")         # always returns str
age   = int(input("Age: "))       # convert immediately
price = float(input("Price: "))

# Integer division
17 // 5    # → 3  (floor division)
17 % 5     # → 2  (remainder/modulo)
divmod(17, 5)  # → (3, 2)  both at once
```

## Gotchas
- `input()` ALWAYS returns a string — convert before math
- `int("3.14")` raises ValueError — use `float()` first
- `//` floors toward negative infinity: `-7 // 2 == -4` not `-3`

## Interview tips
- `//` and `%` are used constantly — time conversion, pagination, even/odd checks
- Wrap `input()` conversion in try/except for robust code
