# Exception Handling

## Try / except
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Can't divide by zero")
except (TypeError, ValueError) as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Unexpected: {e}")
else:
    print("No error occurred")
finally:
    print("Always runs — cleanup here")
```

## Raising
```python
def set_age(age):
    if age < 0:
        raise ValueError(f"Age can't be negative: {age}")
    return age
```

## Custom exceptions
```python
class InsufficientFundsError(Exception):
    def __init__(self, amount, balance):
        self.amount = amount
        self.balance = balance
        super().__init__(f"Can't withdraw {amount}, balance is {balance}")
```

## Common exceptions
| Exception | When |
|-----------|------|
| ValueError | Wrong value |
| TypeError | Wrong type |
| KeyError | Dict key missing |
| IndexError | List index out of range |
| AttributeError | No such attribute |
| FileNotFoundError | File missing |
| ZeroDivisionError | Division by zero |
