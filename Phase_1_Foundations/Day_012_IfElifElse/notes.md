# Day 12 — Quick Reference

## if / else

```python
if condition:
    # runs when condition is True
else:
    # runs when condition is False
```

## if / elif / else

```python
if condition_1:
    # runs when condition_1 is True
elif condition_2:
    # runs when condition_1 is False AND condition_2 is True
elif condition_3:
    # ...
else:
    # runs when none of the above matched
```

Only the **first** matching branch runs. The rest are skipped.

## Comparison operators

```python
x == y    # equal to
x != y    # not equal to
x > y     # greater than
x < y     # less than
x >= y    # greater than or equal to
x <= y    # less than or equal to
```

## Logical operators

```python
x > 0 and x < 10    # True only if BOTH are True
x < 0 or x > 100    # True if EITHER is True
not True             # False  — flips the boolean
```

## Gotchas

- `=` assigns a value. `==` compares. Mixing them up is the most common beginner error.
- `elif` only runs if all previous conditions were False.
- The `else` branch is optional — you don't always need one.
- Indentation defines the block. Everything inside the `if` must be indented by the same amount.
- `0`, `""`, `None`, and empty collections are falsy — they behave like `False` in a condition.
