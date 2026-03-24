# Day 18 — OOP: Classes & Objects

## Key syntax
```python
class MyClass:
    class_attr = "shared"

    def __init__(self, x):
        self.x = x          # instance attribute

    def method(self):       # always takes self
        return self.x

    def __str__(self):      # print(obj)
        return f"MyClass({self.x})"

    def __repr__(self):     # repr(obj)
        return f"MyClass({self.x!r})"

    @classmethod
    def from_dict(cls, d):  # factory method
        return cls(d['x'])

    @staticmethod
    def helper(n):          # utility — no self/cls
        return n * 2
```

## Gotchas
- Every method needs `self` as first param
- `_name` = private by convention (not enforced)
- Class attrs are shared — mutating from instance can surprise you

## Interview tips
- `__str__` for humans, `__repr__` for developers
- `@classmethod` for alternative constructors (`from_string`, `from_dict`)
- Mutable default in `__init__`: `self.items = []` not `def __init__(self, items=[])`
