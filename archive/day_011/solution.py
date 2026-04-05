# Day 011 — OOP: Classes & Objects — REFERENCE SOLUTION

class Person:
    def __init__(self, name: str, age: int):
        # Store as instance attributes — unique to each Person object
        self.name = name
        self.age = age

    def greet(self) -> str:
        # self.name and self.age access this instance's data
        return f"Hi, I am {self.name} and I am {self.age} years old"

    def is_adult(self) -> bool:
        return self.age >= 18

    def __str__(self) -> str:
        # Called by str() and print() — human-readable representation
        return f"Person({self.name}, {self.age})"
