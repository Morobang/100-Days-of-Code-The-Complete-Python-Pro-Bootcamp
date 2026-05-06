# Day 34 — Quick Reference: Dict and Set Comprehensions

## Dict comprehension syntax
```python
{key_expr: val_expr for item in iterable}
{key_expr: val_expr for item in iterable if condition}
```

## Common patterns
```python
# From a range
squares = {n: n**2 for n in range(1, 6)}

# Word → length
lengths = {w: len(w) for w in words}

# From existing dict — transform values
discounted = {k: v * 0.9 for k, v in prices.items()}

# From existing dict — filter
passing = {k: v for k, v in scores.items() if v >= 70}

# Invert a dict
inverted = {v: k for k, v in original.items()}

# Uppercase all keys
upper_keys = {k.upper(): v for k, v in d.items()}

# From two parallel lists
paired = {keys[i]: values[i] for i in range(len(keys))}
```

## Set comprehension syntax
```python
{expression for item in iterable}
{expression for item in iterable if condition}
```

## Set comprehension examples
```python
first_letters = {w[0] for w in words}        # unique first chars
unique_lengths = {len(w) for w in words}      # unique lengths
evens = {n for n in range(20) if n % 2 == 0}
domains = {e.split('@')[1] for e in emails}
```

## Choosing the right comprehension
| Want | Use |
|------|-----|
| Ordered list, allow duplicates | `[...]` |
| Key → value mapping | `{k: v ...}` |
| Unique values, no order needed | `{expr ...}` |
