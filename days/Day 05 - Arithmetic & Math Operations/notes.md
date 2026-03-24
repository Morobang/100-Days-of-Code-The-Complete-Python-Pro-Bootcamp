# Day 05 — Arithmetic & Math Operations

## Key syntax
```python
+  -  *  /    # basic
//             # floor division: 7//2 == 3
%              # modulo: 7%2 == 1
**             # power: 2**10 == 1024

x += 1   x -= 1   x *= 2   x /= 2   x **= 2

round(3.14159, 2)   # 3.14
abs(-5)             # 5
divmod(17, 5)       # (3, 2)
```

## Gotchas
- `/` always returns a float: `4/2 == 2.0`
- `//` floors toward -∞: `-7//2 == -4` not `-3`
- Floating point: `0.1 + 0.2 != 0.3` — use `round()` for display

## Interview tips
- `%` for even/odd, time conversion, wrapping array indices
- `**0.5` is square root — same as `math.sqrt()`
- `divmod(a, b)` gives quotient + remainder in one call
