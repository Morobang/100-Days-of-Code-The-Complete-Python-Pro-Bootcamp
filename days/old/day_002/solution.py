# Day 002 — String Methods — REFERENCE SOLUTION

def caesar_encrypt(text: str, shift: int) -> str:
    # For each character:
    # - if alphabetic, find its offset from 'a' or 'A'
    # - add shift, wrap with % 26, convert back to char
    # - if not alphabetic, leave it unchanged
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result.append(chr((ord(char) - base + shift) % 26 + base))
        else:
            result.append(char)
    return "".join(result)


def caesar_decrypt(text: str, shift: int) -> str:
    # Decryption is just encryption with a negative shift
    return caesar_encrypt(text, -shift)


def word_frequency(text: str) -> dict:
    freq = {}
    for word in text.lower().split():
        word = word.strip(".,!?")   # remove punctuation from each word
        freq[word] = freq.get(word, 0) + 1  # .get with default avoids KeyError
    return freq


def compress(s: str) -> str:
    if not s:
        return ""
    result, i = [], 0
    while i < len(s):
        char, count = s[i], 1
        # count how many times this char repeats consecutively
        while i + count < len(s) and s[i + count] == char:
            count += 1
        result.append(char if count == 1 else f"{char}{count}")
        i += count
    return "".join(result)
