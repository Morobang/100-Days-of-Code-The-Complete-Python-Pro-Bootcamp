# Day 013 — Methods & self — REFERENCE SOLUTION

class Temperature:
    def __init__(self, celsius: float):
        self.celsius = celsius

    def to_fahrenheit(self) -> float:
        return self.celsius * 9/5 + 32

    def to_kelvin(self) -> float:
        return self.celsius + 273.15

    @classmethod
    def from_fahrenheit(cls, f: float):
        # Convert F to C, then create instance
        return cls((f - 32) * 5/9)
