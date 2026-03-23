# Day 19 — OOP: Classes & Objects

## Key syntax
```python
class MyClass:
    class_attr = "shared"           # shared by all instances

    def __init__(self, x, y):       # constructor
        self.x = x                  # instance attribute
        self.y = y

    def method(self):               # instance method
        return self.x + self.y

    def __str__(self):              # print(obj) representation
        return f"MyClass({self.x})"

    def __repr__(self):             # developer repr — should recreate object
        return f"MyClass({self.x!r}, {self.y!r})"

obj = MyClass(1, 2)
obj.method()
print(obj)
```

## Gotchas
- `self` is always the first parameter of instance methods — don't forget it
- `__init__` is NOT `__new__` — it initialises, not creates
- Class attributes are shared — mutating them from an instance can surprise you

## Interview tips
- "What is encapsulation?" → bundling data + methods, hiding internal state
- Use `_name` for "private" attributes (convention, not enforced)
- `__str__` is for humans, `__repr__` is for developers/debugging
