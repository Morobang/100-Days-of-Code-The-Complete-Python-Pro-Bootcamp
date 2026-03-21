# Day 05 — Arithmetic & Math Operations

## Key syntax
```python
+   -   *   /     # basic
//              # floor division — 7 // 2 == 3
%               # modulo/remainder — 7 % 2 == 1
**              # exponent — 2 ** 10 == 1024

# Augmented assignment
x += 1    # x = x + 1
x -= 1
x *= 2
x /= 2
x //= 2
x **= 2

round(3.14159, 2)   # → 3.14
abs(-5)             # → 5
max(1, 2, 3)        # → 3
min(1, 2, 3)        # → 1
```

## Gotchas
- `/` always returns a float: `4 / 2 == 2.0` not `2`
- `//` floors toward negative infinity: `-7 // 2 == -4` not `-3`
- Floating point isn't exact: `0.1 + 0.2 != 0.3` (use `round()` for display)

## Interview tips
- `%` (modulo) is used constantly — check even/odd, wrap indices, time conversion
- `**` for powers — `x ** 0.5` is square root (or use `math.sqrt(x)`)
- Know `divmod(7, 2)` → `(3, 1)` — gives quotient and remainder in one call
