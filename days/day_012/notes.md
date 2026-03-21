# Day 012 — OOP: __init__ & Instance Attributes

## Key syntax
```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self._mileage = 0    # _ prefix = convention for "private"

    def drive(self, km):
        if km < 0:
            raise ValueError("km must be positive")
        self._mileage += km
```

## Gotchas
- Instance attributes defined outside `__init__` are valid but confusing — always define in `__init__`
- `_name` (single underscore) = "please don't touch this from outside" (convention)
- `__name` (double underscore) = name mangling — `MyClass.__name` becomes `_MyClass__name`

## Interview tips
- "Why use `_` prefix?" → signals internal implementation detail, not part of public API
- Data validation in `__init__` / setters prevents invalid state — show you think about correctness
- Know the difference between `__str__` (for users) and `__repr__` (for developers/debugging)
