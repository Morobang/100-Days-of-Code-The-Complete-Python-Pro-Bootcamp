# Decorators & Closures

## Closure
```python
def outer(x):
    def inner(y):   # remembers x
        return x + y
    return inner

add5 = outer(5)
add5(3)    # 8
```

## Basic decorator
```python
from functools import wraps

def logger(func):
    @wraps(func)          # preserves __name__, __doc__
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        return result
    return wrapper

@logger
def greet(name):
    return f"Hello {name}"
```

## Decorator with arguments
```python
def repeat(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hi():
    print("hi")
```

## Common uses
- Logging, timing, auth checks
- `@functools.lru_cache` for memoization
- `@property`, `@classmethod`, `@staticmethod`
