# Day 31 — Quick Reference: Set Operations

## In-place operators (modify the set)
| Operator | Method equivalent | Effect |
|----------|-------------------|--------|
| `a \|= b` | `a.update(b)` | Add all elements of b into a |
| `a &= b` | `a.intersection_update(b)` | Keep only elements in both |
| `a -= b` | `a.difference_update(b)` | Remove elements of b from a |
| `a ^= b` | `a.symmetric_difference_update(b)` | Keep elements in exactly one |

## Non-in-place (return new set, originals unchanged)
```python
a | b    a.union(b)
a & b    a.intersection(b)
a - b    a.difference(b)
a ^ b    a.symmetric_difference(b)
```

## Chaining across 3+ sets
```python
a & b & c               # common to all three
a | b | c               # in any of the three
a - b - c               # in a but not in b or c

# Loop version for N sets
common = sets[0].copy()
for s in sets[1:]:
    common &= s
```

## Relationship tests (return bool)
```python
a.issubset(b)      # every element of a is in b
a.issuperset(b)    # every element of b is in a
a.isdisjoint(b)    # no elements in common
```

## Common patterns
```python
# Filter against a blocklist
clean = words - blocklist

# Elements common to multiple groups
overlap = group1 & group2 & group3

# Deduplicate while iterating
seen = set()
for item in items:
    if item not in seen:
        process(item)
        seen.add(item)
```
