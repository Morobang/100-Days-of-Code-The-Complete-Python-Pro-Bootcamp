# Day 006 — Dictionaries — REFERENCE SOLUTION

def group_by(lst: list, key_fn) -> dict:
    result = {}
    for item in lst:
        # setdefault initialises the key with [] if not present
        result.setdefault(key_fn(item), []).append(item)
    return result


def invert_dict(d: dict) -> dict:
    # Check uniqueness of values before inverting
    if len(set(d.values())) != len(d):
        raise ValueError("Values must be unique to invert dict")
    return {v: k for k, v in d.items()}


def most_common(lst: list):
    # Build frequency dict first
    freq = {}
    for item in lst:
        freq[item] = freq.get(item, 0) + 1
    # max() over the dict uses keys; key=freq.get makes it compare values
    return max(freq, key=freq.get)
