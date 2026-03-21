# Day 011 — OOP: Classes & Objects

## Key syntax
```python
class Dog:
    species = "Canis lupus"      # class attribute — shared by all instances

    def __init__(self, name):    # constructor — called on Dog("Rex")
        self.name = name         # instance attribute — unique per object

    def bark(self):              # method — always takes self as first arg
        return f"{self.name} says woof!"

rex = Dog("Rex")
rex.bark()         # "Rex says woof!"
Dog.species        # "Canis lupus"
rex.species        # also works — looks up class if not on instance
```

## Gotchas
- Forgetting `self` is the #1 beginner OOP mistake — every method needs it
- Class attributes are shared: mutating one from an instance can be surprising
- `__init__` is NOT `__new__` — `__init__` initialises, `__new__` creates the object

## Interview tips
- "What is the difference between a class and an object?" → class is the blueprint, object is the instance
- Know the difference between class attributes and instance attributes
- `self` is just a convention — Python doesn't enforce the name, but always use it
