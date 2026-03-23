# Day 11 — Dictionaries — SOLUTIONS

phonebook = {'Rocket':'083-111-2222','Alice':'072-333-4444','Bob':'061-555-6666'}

def lookup(book, name):
    return book.get(name, 'Not found')

def word_count(sentence):
    counts = {}
    for word in sentence.lower().split():
        word = word.strip('.,!?')
        counts[word] = counts.get(word, 0) + 1
    return counts

def deep_merge(d1, d2):
    result = d1.copy()
    for k, v in d2.items():
        if k in result and isinstance(result[k], dict) and isinstance(v, dict):
            result[k] = deep_merge(result[k], v)
        else:
            result[k] = v
    return result
