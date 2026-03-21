# Day 014 — Dunder / Magic Methods

## Common dunders
```python
__init__      # constructor
__str__       # str(obj), print(obj)
__repr__      # repr(obj), shown in REPL
__len__       # len(obj)
__eq__        # obj == other
__lt__        # obj < other  (also enables sorted())
__add__       # obj + other
__sub__       # obj - other
__mul__       # obj * other
__contains__  # x in obj
__getitem__   # obj[key]
__iter__      # for x in obj
__next__      # next(obj)
__enter__     # with obj: (context manager)
__exit__      # end of with block
```

## Gotchas
- If you define `__eq__`, also define `__hash__` (or set it to None for mutable objects)
- `__repr__` should ideally be valid Python that recreates the object
- Defining `__lt__` alone isn't enough for full sorting — use `@functools.total_ordering`

## Interview tips
- Dunders let your classes feel like built-in types — shows deep Python understanding
- `__enter__`/`__exit__` = context manager protocol (the `with` statement)
- Know that `a + b` calls `a.__add__(b)` — and falls back to `b.__radd__(a)` if that fails
