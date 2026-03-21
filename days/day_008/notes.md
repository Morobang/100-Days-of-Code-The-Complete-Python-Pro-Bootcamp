# Day 008 — Loops

## Key syntax
```python
for i in range(5):        # 0,1,2,3,4
for i in range(2, 8, 2):  # 2,4,6
for i, v in enumerate(lst): ...
for a, b in zip(lst1, lst2): ...

while condition:
    ...
    break     # exit loop
    continue  # skip to next iteration

# List from loop
result = [x**2 for x in range(10)]  # prefer comprehension where possible
```

## Gotchas
- `range(n)` is 0 to n-1, not 0 to n
- `for` loop variable leaks into outer scope in Python (unlike some languages)
- `while True` + `break` is idiomatic for "loop until condition"

## Interview tips
- Sieve of Eratosthenes is the expected answer for "find all primes up to N" — O(n log log n)
- "Power of 2" bit trick: `n & (n-1) == 0` — mention this as the O(1) alternative
- Know `enumerate()` and `zip()` — using them shows Python fluency
