# Day 26 — Generators & Iterators

## Key syntax
```python
# Generator function
def gen():
    yield 1
    yield 2

# Infinite generator
def counter(n=0):
    while True: yield n; n+=1

# Generator expression
gen = (x**2 for x in range(100))

# send() — coroutine pattern
def accumulator():
    total=0
    while True: total+=yield total

# yield from — delegate to sub-generator
def flatten(lst):
    for item in lst:
        if isinstance(item,list): yield from flatten(item)
        else: yield item
```

## Gotchas
- Generator exhausted after one pass — can't reuse
- `next()` on exhausted generator raises `StopIteration`
- `list(gen)` defeats the purpose for large data

## Interview tips
- "Process 10GB CSV?" → generator, line by line
- `yield from` delegates to another generator (Python 3.3+)
- Generator pipelines = lazy ETL — real pattern in data engineering
