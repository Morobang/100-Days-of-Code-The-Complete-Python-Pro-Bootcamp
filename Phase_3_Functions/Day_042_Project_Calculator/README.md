# Day 42: Project — Calculator

**Phase:** 3 — Functions
**Difficulty:** ⭐⭐⭐

## Project description

Build a multi-operation calculator that applies everything from Phase 3 so far: dedicated functions for each operation, a dispatcher function, input validation, and a history feature.

## Requirements

- One function per operation: `add`, `subtract`, `multiply`, `divide`, `power`, `modulo`
- A `calculate(a, operation, b)` function that calls the right operation
- A `get_number(prompt)` function that keeps asking until the user enters a valid number
- Division by zero returns `None` with a clear error message
- A **history** list that stores each calculation as a string
- Menu options: calculate, show history, clear history, quit

## Example session

```
=== Calculator ===
1. Calculate
2. Show history
3. Clear history
4. Quit

Choice: 1
First number: 10
Operation (+, -, *, /, **, %): *
Second number: 5
Result: 10.0 * 5.0 = 50.0

Choice: 2
1. 10.0 * 5.0 = 50.0
```

## Files

| File | Purpose |
|------|---------|
| `starter.py` | Skeleton with TODO comments |
| `solution/calculator.py` | Complete solution |

## Concepts used
Days 1–41 — functions, parameters, return values, default params, loops, dicts
