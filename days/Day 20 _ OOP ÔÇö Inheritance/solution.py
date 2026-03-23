# Day 20 — OOP: Inheritance — SOLUTIONS
import math

class Shape:
    def __init__(self, color='white'):
        self.color = color

    def area(self):
        raise NotImplementedError

    def describe(self):
        name = type(self).__name__
        return f"A {self.color} {name} with area {self.area():.2f}"


class Circle(Shape):
    def __init__(self, radius, color='white'):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height, color='white'):
        super().__init__(color)
        self.width  = width
        self.height = height

    def area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, side, color='white'):
        super().__init__(side, side, color)  # width = height = side
