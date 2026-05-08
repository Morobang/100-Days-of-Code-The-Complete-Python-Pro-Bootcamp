# Exception Handling — Quick Reference

## Basic try / except
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print('Cannot divide by zero')
```

## Catching Specific Exceptions
```python
try:
    value = int(input('Enter a number: '))
except ValueError:
    print('That was not a number')
```

## Getting the Error Message
```python
try:
    int('abc')
except ValueError as e:
    print(f'Error: {e}')   # Error: invalid literal for int()...
```

## Multiple except Blocks
```python
try:
    value = int(input('Enter: '))
    result = 10 / value
except ValueError:
    print('Not a valid number')
except ZeroDivisionError:
    print('Cannot divide by zero')
```

## else — Runs Only If No Exception
```python
try:
    value = int('42')
except ValueError:
    print('Bad input')
else:
    print(f'Got: {value}')   # runs because no exception was raised
```

## finally — Always Runs
```python
try:
    f = open('data.txt')
    data = f.read()
except FileNotFoundError:
    print('File not found')
finally:
    print('Done')            # always prints, with or without exception
```

## Common Exception Types
| Exception | When it occurs |
|-----------|---------------|
| `ValueError` | Right type, wrong value: `int('abc')` |
| `TypeError` | Wrong type: `'a' + 1` |
| `ZeroDivisionError` | Division by zero |
| `FileNotFoundError` | Opening a non-existent file |
| `IndexError` | List index out of range |
| `KeyError` | Dict key not found |
| `AttributeError` | Calling a method that doesn't exist |
