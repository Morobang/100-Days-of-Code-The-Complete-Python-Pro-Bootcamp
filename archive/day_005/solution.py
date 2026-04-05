# Day 005 — Tuples & Sets — REFERENCE SOLUTION

def minmax(lst: list) -> tuple:
    # Built-ins min() and max() are O(n) each
    # Return as tuple — natural fit for multiple return values
    return (min(lst), max(lst))


def unzip(pairs: list) -> tuple:
    # zip(*pairs) is the idiomatic Python unzip
    # The * unpacks the list of pairs as separate arguments to zip
    # map(list, ...) converts the zip result to lists
    firsts, seconds = zip(*pairs)
    return list(firsts), list(seconds)


def common_elements(a: list, b: list) -> list:
    # Set intersection: O(min(len(a), len(b)))
    return list(set(a) & set(b))


def unique_to_first(a: list, b: list) -> list:
    # Set difference: elements in a that are not in b
    return list(set(a) - set(b))
