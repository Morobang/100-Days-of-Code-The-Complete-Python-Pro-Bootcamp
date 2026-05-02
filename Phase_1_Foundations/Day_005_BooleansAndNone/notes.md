# Day 5 — Quick Reference

## Booleans

```python
is_raining = True
is_sunny = False
print(type(True))   # <class 'bool'>
```

## bool() — convert to boolean

```python
bool(1)        # True
bool(0)        # False
bool("hello")  # True
bool("")       # False  (empty string)
bool(None)     # False
bool(-5)       # True   (any non-zero number is True)
```

## Truthy vs falsy

| Falsy (converts to False) | Truthy (converts to True) |
|---------------------------|---------------------------|
| `0` | Any non-zero number |
| `""` (empty string) | Any non-empty string |
| `None` | Any object |
| `False` | `True` |

## None

```python
result = None         # variable exists but has no value
print(result)         # None
print(type(result))   # <class 'NoneType'>
```

## Gotchas

- `True` and `False` are capitalized — `true` and `false` will error
- `None` is not the same as `0`, `False`, or `""` — it is its own type (`NoneType`)
- `bool("False")` is `True` — because the string is non-empty. The content doesn't matter.
- When a function doesn't explicitly return anything, it returns `None`
