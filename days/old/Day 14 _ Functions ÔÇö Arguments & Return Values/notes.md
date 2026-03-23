# Day 14 — Functions: Arguments & Return Values

## Key syntax
```python
def fn(pos_arg, default=value, *args, **kwargs):
    pass

# Positional vs keyword
fn(1, 2)                  # positional
fn(a=1, b=2)              # keyword
fn(1, b=2)                # mixed

# *args — any number of positional args (tuple inside fn)
def total(*args): return sum(args)
total(1, 2, 3, 4)

# **kwargs — any number of keyword args (dict inside fn)
def display(**kwargs):
    for k, v in kwargs.items(): print(k, v)
display(name='Rocket', score=9500)

# Returning functions (closures)
def make_adder(n):
    def add(x):
        return x + n
    return add

add5 = make_adder(5)
add5(3)   # 8
```

## Gotchas
- Default mutable args are shared across calls: `def fn(lst=[])` is a bug — use `None`
- `*args` must come before `**kwargs` in the signature
- Keyword args can be passed in any order

## Interview tips
- Returning a function from a function = **closure** — comes up a lot
- `*args`/`**kwargs` shows you can write flexible, reusable APIs
- Know `functools.partial` — pre-fills arguments of a function
