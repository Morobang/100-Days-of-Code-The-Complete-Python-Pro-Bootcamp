# Day 010 — Functions: *args, **kwargs & Returns

## Key syntax
```python
def fn(*args):          # args is a tuple
    print(args)

def fn(**kwargs):       # kwargs is a dict
    print(kwargs)

def fn(*args, **kwargs):
    pass

# Unpacking when calling
fn(*[1,2,3])            # same as fn(1,2,3)
fn(**{'a':1,'b':2})     # same as fn(a=1,b=2)

# Type hints
def greet(name: str, age: int = 0) -> str:
    ...

# Docstring (Google style)
def fn(x: int) -> int:
    """One-line summary.

    Args:
        x: Description of x.

    Returns:
        Description of return value.
    """
```

## Gotchas
- `*args` must come before `**kwargs` in the signature
- You can mix positional + *args: `def fn(a, b, *rest)` — rest catches overflow
- Unpacking with `*` and `**` works in function calls AND in assignments

## Interview tips
- "Write a function that accepts any number of args" → *args/*kwargs pattern
- Type hints are not enforced at runtime — they're for readability and tooling
- Google-style docstrings are the standard in data engineering codebases
