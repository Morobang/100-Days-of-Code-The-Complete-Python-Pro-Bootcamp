# Raising Exceptions — Quick Reference

## raise
```python
raise ValueError('n must be positive')
raise TypeError('expected a string')
raise FileNotFoundError('config.txt is missing')
```
You can raise any built-in exception with a custom message.

## Using raise for Validation
```python
def get_positive(n):
    if n <= 0:
        raise ValueError(f'{n} must be positive')
    return n
```
The caller catches it or lets it propagate — either way, invalid input is rejected.

## Re-raising with bare `raise`
Inside an `except` block, `raise` with no arguments re-raises the current exception unchanged.
```python
def wrapper():
    try:
        risky()
    except RuntimeError:
        log_error()   # do something, then...
        raise         # let the exception continue propagating
```

## raise vs return None

| Situation | Prefer |
|-----------|--------|
| Caller passed invalid input — their bug | `raise` |
| Something that genuinely should never happen | `raise` |
| Missing data that a caller might legitimately handle | `return None` |
| Optional feature not available | `return None` |

## Common Built-in Exceptions to Raise
| Exception | When to use it |
|-----------|---------------|
| `ValueError` | Right type, wrong value |
| `TypeError` | Wrong type |
| `FileNotFoundError` | Required file is missing |
| `RuntimeError` | General unexpected error |
| `NotImplementedError` | Method stub not yet written |
