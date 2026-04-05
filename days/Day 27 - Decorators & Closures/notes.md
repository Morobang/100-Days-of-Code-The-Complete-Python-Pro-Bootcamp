# Day 27 — Decorators & Closures

## Key syntax
```python
from functools import wraps

# Closure
def outer(x):
    def inner(y): return x+y   # inner remembers x
    return inner

# Basic decorator
def my_dec(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        # before
        result=func(*args,**kwargs)
        # after
        return result
    return wrapper

# Decorator with args
def repeat(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            for _ in range(n): func(*args,**kwargs)
        return wrapper
    return decorator

@repeat(3)
def hi(): print('hi')
```

## Gotchas
- Always use `@wraps(func)` — preserves `__name__` and `__doc__`
- Stacking decorators applies bottom-up: `@a @b def fn` → `a(b(fn))`
- `@decorator` is syntactic sugar for `fn = decorator(fn)`

## Interview tips
- Real uses: logging, timing, auth, rate limiting, caching
- `@functools.lru_cache` is built-in memoization
- Flask/Django use decorators everywhere: `@app.route`, `@login_required`
