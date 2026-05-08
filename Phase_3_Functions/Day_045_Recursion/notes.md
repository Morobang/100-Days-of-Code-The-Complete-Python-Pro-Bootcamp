# Recursion — Quick Reference

## The Two Rules
Every recursive function needs exactly two things:

| Part | What it does |
|------|-------------|
| **Base case** | Stops the recursion — returns a value directly |
| **Recursive case** | Calls itself with a *simpler* input, moving toward the base case |

## Basic Pattern
```python
def recursive(n):
    if n == 0:          # base case — stop here
        return 0
    return n + recursive(n - 1)  # recursive case — smaller problem
```

## How the Call Stack Works
Each recursive call adds a new frame to the call stack.
When a call returns, its frame is removed and the result goes back to the caller.

```
factorial(3)
  → 3 * factorial(2)
        → 2 * factorial(1)
              → 1 * factorial(0)
                    → 1          ← base case
              ← 1 * 1 = 1
        ← 2 * 1 = 2
  ← 3 * 2 = 6
```

## Classic Examples
```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def sum_list(lst):
    if not lst:
        return 0
    return lst[0] + sum_list(lst[1:])

def countdown(n):
    if n < 0:
        return
    print(n)
    countdown(n - 1)
```

## Recursion vs Iteration
- Recursion is cleaner when the problem is **naturally self-similar** (trees, nested structures)
- Iteration is usually faster and avoids stack overflow for large inputs
- Both can solve the same problems

## Depth Limit
Python limits recursion to ~1 000 calls by default.
Exceeding it raises `RecursionError: maximum recursion depth exceeded`.

```python
import sys
print(sys.getrecursionlimit())  # 1000
```
