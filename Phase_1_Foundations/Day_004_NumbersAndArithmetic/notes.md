# Day 4 — Quick Reference

## Number types

```python
x = 42       # int — whole number
y = 3.14     # float — decimal number
type(x)      # <class 'int'>
type(y)      # <class 'float'>
```

## Arithmetic operators

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `+` | Addition | `5 + 3` | `8` |
| `-` | Subtraction | `5 - 3` | `2` |
| `*` | Multiplication | `5 * 3` | `15` |
| `/` | Division (always float) | `10 / 3` | `3.333...` |
| `//` | Integer division | `10 // 3` | `3` |
| `%` | Modulo (remainder) | `10 % 3` | `1` |
| `**` | Exponentiation | `2 ** 8` | `256` |

## Integer division vs true division

```python
10 / 3    # 3.3333... (always float, even if result is whole)
10 // 3   # 3 (floor division — truncates decimal)
7 / 2     # 3.5
7 // 2    # 3
```

## Modulo use cases

```python
10 % 3    # 1  — remainder after dividing 10 by 3
15 % 5    # 0  — 15 divides evenly by 5
7 % 2     # 1  — odd numbers have remainder 1 when divided by 2
8 % 2     # 0  — even numbers have remainder 0
```

## math module

```python
import math

math.sqrt(16)    # 4.0
math.pi          # 3.141592653589793
math.floor(4.9)  # 4  — round down
math.ceil(4.1)   # 5  — round up
math.abs(-5)     # use built-in abs() instead: abs(-5) = 5
```

## Gotchas

- `10 / 2` gives `5.0` (a float), not `5` (an int). Use `//` if you need an integer.
- `int(3.9)` gives `3`, not `4`. It truncates, it does not round. Use `round()` to round.
- Division by zero raises a `ZeroDivisionError`.
