# Day 004 — List Methods & Slicing — REFERENCE SOLUTION

def deduplicate(lst: list) -> list:
    # Track what we've seen with a set (O(1) lookup)
    # Build result list maintaining original order
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def flatten_one(lst: list) -> list:
    # For each element: if it's a list, extend (unpack one level)
    # Otherwise just append it as-is
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(item)
        else:
            result.append(item)
    return result


def transpose(matrix: list) -> list:
    # Outer list comp iterates over column indices
    # Inner list comp picks that column's value from each row
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]
