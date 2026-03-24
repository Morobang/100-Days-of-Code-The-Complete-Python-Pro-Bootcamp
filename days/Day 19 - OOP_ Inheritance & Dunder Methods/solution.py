# Day 19 — Inheritance & Dunders — SOLUTIONS
import math

class Shape:
    def __init__(self, color='white'):
        self.color = color
    def area(self): raise NotImplementedError
    def describe(self):
        return f"A {self.color} {type(self).__name__} with area {self.area():.2f}"
    def __gt__(self, o): return self.area() > o.area()
    def __lt__(self, o): return self.area() < o.area()
    def __eq__(self, o): return self.area() == o.area()

class Circle(Shape):
    def __init__(self, radius, color='white'):
        super().__init__(color); self.radius = radius
    def area(self): return math.pi * self.radius**2

class Rectangle(Shape):
    def __init__(self, w, h, color='white'):
        super().__init__(color); self.width=w; self.height=h
    def area(self): return self.width * self.height

class Square(Rectangle):
    def __init__(self, side, color='white'):
        super().__init__(side, side, color)
