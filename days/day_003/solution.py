# Day 003 — Lists — REFERENCE SOLUTION

def second_largest(lst: list) -> int:
    # set() removes duplicates, sorted() gives us order
    # index -2 from the end = second largest
    unique = sorted(set(lst))
    if len(unique) < 2:
        raise ValueError("Need at least 2 unique values")
    return unique[-2]


def rotate(lst: list, n: int) -> list:
    if not lst:
        return lst
    # Modulo handles cases where n > len(lst)
    n = n % len(lst)
    if n == 0:
        return lst[:]
    # Last n elements come first, rest follow
    return lst[-n:] + lst[:-n]


def chunk(lst: list, size: int) -> list:
    # range steps by 'size', slicing gives each chunk
    return [lst[i:i+size] for i in range(0, len(lst), size)]
