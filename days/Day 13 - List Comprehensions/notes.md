# Day 13 — List Comprehensions

## Key syntax
```python
[expr for x in iterable]
[expr for x in iterable if condition]
{k: v for x in iterable}
{expr for x in iterable}          # set
(expr for x in iterable)          # generator (lazy)

# Nested (flatten)
[x for row in matrix for x in row]
```

## Gotchas
- Generator `(x for x in ...)` is consumed once — can't reuse
- Don't nest more than 2 levels — use a regular loop for clarity
- Comprehensions create a NEW collection — original unchanged

## Interview tips
- 30–50% faster than equivalent for + append loop
- "Filter and transform in one line" → comprehension with `if`
- Know when NOT to use them: side effects, complex logic, deep nesting
