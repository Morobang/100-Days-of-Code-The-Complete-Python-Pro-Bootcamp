# Day 10 — Lists — SOLUTIONS

# Exercise 1 — leaderboard
players = [('Rocket', 9500), ('Bob', 7200), ('Alice', 8700)]
sorted_players = sorted(players, key=lambda p: p[1], reverse=True)
for i, (name, score) in enumerate(sorted_players, 1):
    print(f"{i}. {name} — {score}")

# Exercise 2 — remove duplicates preserving order
def remove_duplicates(lst: list) -> list:
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

# Exercise 3 — stats
def stats(numbers: list) -> dict:
    return {
        'min': min(numbers),
        'max': max(numbers),
        'sum': sum(numbers),
        'average': round(sum(numbers) / len(numbers), 2),
    }
