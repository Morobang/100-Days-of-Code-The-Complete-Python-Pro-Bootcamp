# Day 33 — Quick Reference: List Comprehensions

## Syntax
```python
[expression for item in iterable]
[expression for item in iterable if condition]
```

## Common patterns
```python
# Transform
squares   = [n**2 for n in range(10)]
uppercased = [w.upper() for w in words]
lengths   = [len(w) for w in words]

# Filter
positives  = [n for n in nums if n > 0]
long_words = [w for w in words if len(w) > 4]

# Transform + filter
pos_sq = [n**2 for n in nums if n > 0]
passing = [name for name, score in pairs if score >= 70]

# From .items()
in_stock = [k for k, v in d.items() if v > 0]

# From a string
digits = [ch for ch in s if ch.isdigit()]
```

## Nested comprehensions
```python
# Flatten a 2D list
flat = [val for row in matrix for val in row]

# Build a 2D grid
grid = [[0 for _ in range(cols)] for _ in range(rows)]
```

## Tuple unpacking in comprehensions
```python
scores = [('Alice', 88), ('Bob', 75)]
names  = [name for name, score in scores]
labels = [f'{name}: {score}' for name, score in scores]
```

## When to use
- Simple transforms: yes
- Simple filters: yes
- Both together (short): yes
- Side effects (printing, appending): no — use a for loop
- Complex multi-step logic: no — use a for loop
