# Day 10 — Quick Reference

## f-string basics

```python
name = 'Alice'
age = 30
print(f'Name: {name}, Age: {age}')   # Name: Alice, Age: 30
print(f'Next year: {age + 1}')        # Next year: 31
print(f'Upper: {name.upper()}')       # Upper: ALICE
```

## Number formatting

```python
price = 12.5

# Decimal places
print(f'{price:.2f}')    # 12.50
print(f'{price:.4f}')    # 12.5000

# Thousands separator
big = 1234567
print(f'{big:,}')        # 1,234,567

# Percentage (value must be a decimal like 0.85, not 85)
ratio = 0.856
print(f'{ratio:.2%}')    # 85.60%
```

## Alignment

```python
name = 'Alice'
print(f'|{name:<15}|')   # |Alice          |  — left-align in 15 chars
print(f'|{name:>15}|')   # |          Alice|  — right-align
print(f'|{name:^15}|')   # |     Alice     |  — center
```

## Fill characters

```python
print(f'{42:0>5}')        # 00042 — zero-filled, right-aligned, width 5
print(f'{"hi":*^10}')     # ****hi****
```

## Triple-quoted strings

```python
message = """
Line one
Line two
Line three
"""
print(message)
```

## Gotchas

- `:.2f` rounds for display only — the variable's value is unchanged.
- `:.2%` expects a decimal (0.85), not 85 — it multiplies by 100 then adds `%`.
- Alignment width counts the full field: `f'{"hi":>5}'` → `'   hi'` (3 spaces + 2 chars = 5).
- f-strings can contain any Python expression: `f'{2 ** 10}'` → `'1024'`.
