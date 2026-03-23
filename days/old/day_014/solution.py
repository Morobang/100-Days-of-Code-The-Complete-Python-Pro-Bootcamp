# Day 014 — Dunder Methods — REFERENCE SOLUTION
import math

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):    return Vector2D(self.x + other.x, self.y + other.y)
    def __sub__(self, other):    return Vector2D(self.x - other.x, self.y - other.y)
    def __mul__(self, scalar):   return Vector2D(self.x * scalar, self.y * scalar)
    def __len__(self):           return 2
    def __eq__(self, other):     return self.x == other.x and self.y == other.y
    def __str__(self):           return f"Vector2D({self.x}, {self.y})"
    def __repr__(self):          return self.__str__()
    def magnitude(self):         return math.sqrt(self.x**2 + self.y**2)
