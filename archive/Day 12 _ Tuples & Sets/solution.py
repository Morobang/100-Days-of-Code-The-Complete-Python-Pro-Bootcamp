# Day 12 — Tuples & Sets — SOLUTIONS

# Exercise 1 — deduplicate preserving order
def unique(lst: list) -> list:
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


# Exercise 2 — common friends
rocket_friends = {'Alice', 'Bob', 'Charlie', 'Dave'}
alice_friends  = {'Bob', 'Charlie', 'Eve', 'Frank'}

common       = rocket_friends & alice_friends
only_rocket  = rocket_friends - alice_friends
only_alice   = alice_friends - rocket_friends

print("Common:", common)
print("Only Rocket's:", only_rocket)
print("Only Alice's:", only_alice)


# Exercise 3 — top scorer
def top_scorer(players: list) -> str:
    # max() with key= finds the tuple with the highest score (index 1)
    best_name, best_score = max(players, key=lambda p: p[1])
    return best_name
