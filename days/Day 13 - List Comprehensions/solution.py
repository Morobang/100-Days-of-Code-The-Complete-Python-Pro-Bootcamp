# Day 13 — List Comprehensions — SOLUTIONS

celsius = [0, 50, 100, 25, 37, 200, -10]
hot = [round(c*9/5+32, 1) for c in celsius if c*9/5+32 > 100]
print(hot)

def count_chars(s):
    return {char: s.count(char) for char in set(s)}

def unique_flatten(lst_of_lsts):
    seen, result = set(), []
    for item in (x for lst in lst_of_lsts for x in lst):
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
