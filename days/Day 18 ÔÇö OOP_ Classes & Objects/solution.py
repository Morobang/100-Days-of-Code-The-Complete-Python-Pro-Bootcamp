# Day 18 — OOP: Classes & Objects — SOLUTIONS

class Student:
    def __init__(self, name, student_id):
        self.name       = name
        self.student_id = student_id
        self.grades     = []

    def add_grade(self, score): self.grades.append(score)
    def average(self): return sum(self.grades)/len(self.grades) if self.grades else 0
    def __str__(self): return f"Student({self.name}, ID:{self.student_id}, avg:{self.average()})"

class Counter:
    def __init__(self, start=0): self._n = start
    def increment(self, by=1):   self._n += by
    def decrement(self, by=1):   self._n -= by
    def reset(self):             self._n = 0
    @property
    def value(self): return self._n

class Temperature:
    def __init__(self, celsius):
        self.celsius = float(celsius)

    def to_fahrenheit(self): return self.celsius * 9/5 + 32
    def to_kelvin(self):     return self.celsius + 273.15
    def __str__(self):       return f"{self.celsius}°C"
    def __eq__(self, other): return self.celsius == other.celsius
    def __lt__(self, other): return self.celsius < other.celsius

    @classmethod
    def from_fahrenheit(cls, f):
        return cls((f - 32) * 5/9)
