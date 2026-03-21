# Day 09 — Functions — SOLUTIONS
import math

def area_circle(r):
    return round(math.pi * r ** 2, 2)

def area_rectangle(w, h):
    return round(w * h, 2)

def area_triangle(b, h):
    return round(0.5 * b * h, 2)

def is_valid_password(password: str) -> bool:
    if len(password) < 8:
        return False
    has_digit = any(c.isdigit() for c in password)
    has_upper = any(c.isupper() for c in password)
    return has_digit and has_upper

def caesar(text: str, shift: int) -> str:
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result.append(chr((ord(char) - base + shift) % 26 + base))
        else:
            result.append(char)
    return "".join(result)
