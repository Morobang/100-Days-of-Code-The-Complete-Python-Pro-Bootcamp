# Object-Oriented Programming

## Class basics
```python
class Dog:
    species = "Canis lupus"  # class attribute

    def __init__(self, name, breed):
        self.name = name        # instance attributes
        self.breed = breed

    def bark(self):
        return f"{self.name} says woof!"
```

## Dunder methods
```python
def __str__(self):          # str() and print()
def __repr__(self):         # dev representation
def __add__(self, other):   # + operator
def __len__(self):          # len()
def __eq__(self, other):    # == operator
def __lt__(self, other):    # < operator
def __contains__(self, item): # in operator
```

## Inheritance
```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # call parent init
        self.breed = breed

    def speak(self):            # override
        return f"{self.name} says woof"
```

## Properties
```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius must be positive")
        self._radius = value
```

## Class & static methods
```python
@classmethod
def from_string(cls, s):    # factory method
    ...

@staticmethod
def helper(x):              # utility, no self or cls
    return x * 2
```
