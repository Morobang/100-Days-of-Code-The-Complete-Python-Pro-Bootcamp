# Day 10 — Lists — SOLUTIONS

def stats(numbers):
    return {
        'min': min(numbers),
        'max': max(numbers),
        'sum': sum(numbers),
        'average': round(sum(numbers)/len(numbers), 2),
    }

def unique(lst):
    seen, result = set(), []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

def rotate(lst, n):
    if not lst: return lst
    n = n % len(lst)
    return lst[-n:] + lst[:-n] if n else lst[:]
