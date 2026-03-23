# Day 13 — List Comprehensions

## Key syntax
```python
# Basic
[expr for item in iterable]

# With filter
[expr for item in iterable if condition]

# Nested (flatten)
[x for row in matrix for x in row]

# Dict comprehension
{k: v for item in iterable}

# Set comprehension
{expr for item in iterable}

# Generator (lazy — no brackets)
(expr for item in iterable)
```

## Gotchas
- Comprehensions create a NEW list — the original is unchanged
- Nested comprehensions read left to right: outer loop first, inner loop second
- Don't use comprehensions for complex logic — a regular for loop is clearer

## Interview tips
- List comprehensions are 30–50% faster than equivalent for loops
- "Filter and transform in one line" → comprehension with `if`
- Know when NOT to use them — deeply nested or side-effect logic → use a loop
