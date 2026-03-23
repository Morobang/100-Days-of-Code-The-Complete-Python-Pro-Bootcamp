# Day 03 — String Manipulation — SOLUTIONS

def reverse(s: str) -> str:
    return s[::-1]


def count_vowels(s: str) -> int:
    return sum(1 for c in s.lower() if c in "aeiou")


def to_title(s: str) -> str:
    words = s.split()
    return " ".join(word[0].upper() + word[1:] for word in words)


def initials(full_name: str) -> str:
    parts = full_name.split()
    return ".".join(p[0].upper() for p in parts)
