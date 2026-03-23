# Day 20 — OOP: Inheritance

## Key syntax
```python
class Child(Parent):
    def __init__(self, x, y):
        super().__init__(x)      # call parent __init__
        self.y = y               # child-specific

    def method(self):            # override parent method
        parent_result = super().method()  # call parent's version
        return parent_result + " extra"

isinstance(obj, ClassName)   # True if obj is instance of class or subclass
issubclass(Child, Parent)    # True if Child inherits from Parent
type(obj).__name__           # exact class name as string
```

## Gotchas
- Always call `super().__init__(...)` when overriding `__init__` — or parent setup is skipped
- `isinstance(dog, Animal)` is True — use this, not `type(dog) == Animal`
- Python supports multiple inheritance — `class C(A, B)` — use carefully

## Interview tips
- "What is the difference between inheritance and composition?" — classic design question
- "Favour composition over inheritance" is a well-known principle — know what it means
- `super()` is not just for `__init__` — you can call any parent method with it
