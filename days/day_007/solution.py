# Day 007 — Control Flow — REFERENCE SOLUTION

def fizzbuzz(n: int) -> list:
    result = []
    for i in range(1, n + 1):
        # Check most specific condition first (divisible by both)
        if i % 15 == 0:   result.append("FizzBuzz")
        elif i % 3 == 0:  result.append("Fizz")
        elif i % 5 == 0:  result.append("Buzz")
        else:             result.append(str(i))
    return result


def collatz(n: int) -> list:
    seq = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        seq.append(n)
    return seq


def grade(score: int) -> str:
    # Chain of elif — order matters, most restrictive first
    if score >= 90:   return 'A'
    elif score >= 80: return 'B'
    elif score >= 70: return 'C'
    elif score >= 60: return 'D'
    else:             return 'F'


def bmi_category(bmi: float) -> str:
    if bmi < 18.5:  return 'Underweight'
    elif bmi < 25:  return 'Normal'
    elif bmi < 30:  return 'Overweight'
    else:           return 'Obese'
