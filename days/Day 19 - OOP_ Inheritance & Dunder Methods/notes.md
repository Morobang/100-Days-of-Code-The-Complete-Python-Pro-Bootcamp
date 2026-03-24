# Day 19 — OOP: Inheritance & Dunder Methods

## Key syntax
```python
class Child(Parent):
    def __init__(self, x, y):
        super().__init__(x)    # call parent
        self.y = y

    def method(self):          # override

isinstance(obj, Class)        # True if obj is instance (or subclass)
issubclass(Child, Parent)

# Common dunders
__str__    __repr__   __len__
__eq__     __lt__     __le__    __gt__    __ge__
__add__    __sub__    __mul__   __truediv__
__contains__   __getitem__   __iter__
```

## Gotchas
- Always call `super().__init__()` when overriding `__init__`
- Use `isinstance(x, Class)` not `type(x) == Class`
- Define `__eq__` + `__lt__` → `sorted()` works

## Interview tips
- "Composition vs inheritance?" — know the tradeoff
- `type(self).__name__` gives exact class name as string
- `@functools.total_ordering` fills in all comparison dunders from just `__eq__` + `__lt__`
