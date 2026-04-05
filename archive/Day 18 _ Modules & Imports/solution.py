# Day 18 — Modules & Imports — SOLUTIONS
import random, string
from datetime import date

# Exercise 1
def generate_password(length: int = 12) -> str:
    chars = string.ascii_letters + string.digits + string.punctuation
    # random.choices allows repeats — sample doesn't
    return ''.join(random.choices(chars, k=length))


# Exercise 2
def days_until_birthday(month: int, day: int) -> int:
    today = date.today()
    next_birthday = date(today.year, month, day)
    if next_birthday < today:
        next_birthday = date(today.year + 1, month, day)
    return (next_birthday - today).days


# Exercise 3
def quiz(questions: dict, n: int = 3):
    selected = random.sample(list(questions.items()), min(n, len(questions)))
    correct = 0
    for question, answer in selected:
        user = input(f'{question} ').strip()
        if user.lower() == answer.lower():
            print('✅ Correct!')
            correct += 1
        else:
            print(f'❌ Wrong — answer was {answer}')
    print(f'\nScore: {correct}/{len(selected)}')
