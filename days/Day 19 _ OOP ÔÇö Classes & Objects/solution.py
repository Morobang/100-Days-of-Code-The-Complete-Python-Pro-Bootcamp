# Day 19 — OOP: Classes & Objects — SOLUTIONS

class Student:
    def __init__(self, name: str, student_id: str):
        self.name       = name
        self.student_id = student_id
        self.grades     = []            # mutable default must be in __init__

    def add_grade(self, score: float):
        self.grades.append(score)

    def average(self) -> float:
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def __str__(self) -> str:
        return f"Student({self.name}, ID:{self.student_id}, avg:{self.average()})"


class Counter:
    def __init__(self, start: int = 0):
        self._count = start

    def increment(self, by: int = 1):
        self._count += by

    def decrement(self, by: int = 1):
        self._count -= by

    def reset(self):
        self._count = 0

    @property
    def value(self) -> int:
        return self._count

    def __str__(self) -> str:
        return f"Counter({self._count})"
