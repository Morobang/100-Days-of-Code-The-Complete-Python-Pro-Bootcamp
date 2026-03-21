# Day 013 — OOP: Methods & self

## Key syntax
```python
class Foo:
    def instance_method(self):    # regular method — gets the instance
        return self.x

    @classmethod
    def class_method(cls):        # gets the class — factory methods
        return cls()

    @staticmethod
    def static_method(x):         # no self or cls — pure utility
        return x * 2
```

## Gotchas
- `@classmethod` is the right pattern for alternative constructors (`from_dict`, `from_string`)
- `@staticmethod` when you don't need access to the class or instance at all
- Calling an instance method without `self` in the signature raises `TypeError`

## Interview tips
- "How do you create multiple ways to instantiate a class?" → `@classmethod` factory methods
- `datetime.fromisoformat()`, `int.from_bytes()` are real stdlib examples of this pattern
