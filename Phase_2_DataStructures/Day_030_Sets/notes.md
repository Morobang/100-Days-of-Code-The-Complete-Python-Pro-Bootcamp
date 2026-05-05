# Day 30 — Quick Reference: Sets

## Creating sets
```python
s = {1, 2, 3}              # literal
s = set([1, 2, 2, 3])      # from list — removes duplicates
s = set('hello')           # from string — unique chars
s = set()                  # empty set — {} creates an empty dict!
```

## Modifying
```python
s.add(x)          # add one element (ignored if duplicate)
s.update(iter)    # add all elements from an iterable
s.remove(x)       # remove x — KeyError if missing
s.discard(x)      # remove x — no error if missing (prefer this)
s.pop()           # remove and return an arbitrary element
s.clear()         # empty the set
```

## Set operations
| Operation | Operator | Method |
|-----------|----------|--------|
| Union (all) | `a \| b` | `a.union(b)` |
| Intersection (common) | `a & b` | `a.intersection(b)` |
| Difference (a not b) | `a - b` | `a.difference(b)` |
| Symmetric diff (one not both) | `a ^ b` | `a.symmetric_difference(b)` |

## Relationship tests
```python
a.issubset(b)      # every element of a is in b  (a <= b)
a.issuperset(b)    # every element of b is in a  (a >= b)
a.isdisjoint(b)    # no elements in common
```

## Membership (fast)
```python
x in s       # True / False — O(1)
x not in s
```

## Useful patterns
```python
unique = set(my_list)              # remove duplicates
duplicates_removed = len(my_list) - len(unique)
sorted_unique = sorted(unique)     # set → sorted list
```

## frozenset (immutable)
```python
fs = frozenset([1, 2, 3])  # cannot add/remove elements
# can be used as a dict key or element of another set
```
