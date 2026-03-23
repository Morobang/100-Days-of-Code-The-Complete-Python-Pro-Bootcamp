# Day 20 — Modules & pip — SOLUTIONS
import random, string, os
from datetime import date

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(chars, k=length))

def days_until_birthday(month, day):
    today = date.today()
    next_bd = date(today.year, month, day)
    if next_bd < today:
        next_bd = date(today.year + 1, month, day)
    return (next_bd - today).days

def list_py_files(directory):
    return sorted(f for f in os.listdir(directory) if f.endswith('.py'))
