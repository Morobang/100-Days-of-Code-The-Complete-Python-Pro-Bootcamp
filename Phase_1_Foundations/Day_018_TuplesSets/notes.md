# Day 18 — Quick Reference

## Tuples

```python
# Create with parentheses (or just commas)
point = (10, 25)
person = ('Alice', 30, 'Cape Town')
single = (42,)           # single-item tuple needs a trailing comma

# Indexing — same as lists
person[0]    # 'Alice'
person[-1]   # 'Cape Town'

# Unpacking
name, age, city = person

# Tuples are IMMUTABLE — you cannot change them
# person[0] = 'Bob'   # TypeError!
```

**When to use tuples:** fixed data that should not change — coordinates, RGB colours, database rows, function returns with multiple values.

## Sets

```python
# Create with curly braces
fruits = {'apple', 'banana', 'cherry'}
empty_set = set()          # NOT {} — that creates an empty dict!

# Convert list to set (removes duplicates)
nums = [1, 2, 2, 3, 1]
unique = set(nums)         # {1, 2, 3}

# Membership check — very fast
'apple' in fruits          # True

# Adding and removing
fruits.add('mango')        # add one item
fruits.remove('banana')    # removes — raises KeyError if not found
fruits.discard('banana')   # removes — NO error if not found
```

## Set operations

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

a | b    # union        → {1, 2, 3, 4, 5, 6}  — all items
a & b    # intersection → {3, 4}               — items in both
a - b    # difference   → {1, 2}               — in a but not b
```

## Gotchas

- Sets are **unordered** — you cannot index them (`s[0]` raises TypeError).
- `{}` creates an empty dict, not a set. Use `set()` for an empty set.
- `.remove()` raises KeyError if the item is missing; `.discard()` does not.
- Tuples with one item need a trailing comma: `(42,)` not `(42)`.
