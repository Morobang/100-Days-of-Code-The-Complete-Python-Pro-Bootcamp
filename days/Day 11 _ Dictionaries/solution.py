# Day 11 — Dictionaries — SOLUTIONS

# Exercise 1
phonebook = {
    'Rocket': '083-111-2222',
    'Alice':  '072-333-4444',
    'Bob':    '061-555-6666',
}

def lookup(book: dict, name: str) -> str:
    # .get() returns None if missing — we set a default of 'Not found'
    return book.get(name, 'Not found')


# Exercise 2
def word_count(sentence: str) -> dict:
    counts = {}
    for word in sentence.lower().split():
        counts[word] = counts.get(word, 0) + 1
    return counts


# Exercise 3
def invert(d: dict) -> dict:
    # Dict comprehension — swap key and value
    return {v: k for k, v in d.items()}
