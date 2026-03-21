# Day 001 — String Basics — REFERENCE SOLUTION
# Read this ONLY after attempting the notebook yourself.

# ── THOUGHT PROCESS ──────────────────────────────────────────────────────────

def reverse_string(s: str) -> str:
    # Python slicing: [start:stop:step]
    # Omitting start and stop means "entire string"
    # step = -1 means walk backwards → gives us the reverse
    return s[::-1]


def count_vowels(s: str) -> int:
    # Normalise to lowercase so 'A' and 'a' both count
    # Generator expression: iterate chars, yield 1 for each vowel
    # sum() adds them all up — clean and readable
    return sum(1 for c in s.lower() if c in "aeiou")


def is_palindrome(s: str) -> bool:
    # Normalise case first — "Racecar" should pass
    cleaned = s.lower()
    # A string is a palindrome if it equals its own reverse
    return cleaned == cleaned[::-1]
