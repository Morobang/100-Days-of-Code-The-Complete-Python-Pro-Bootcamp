# Day 12 — Tuples & Sets — SOLUTIONS

def unique(lst):
    seen, result = set(), []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

rocket_friends = {'Alice','Bob','Charlie','Dave'}
alice_friends  = {'Bob','Charlie','Eve','Frank'}
print("Common:", rocket_friends & alice_friends)
print("Only Rocket's:", rocket_friends - alice_friends)
print("Only Alice's:", alice_friends - rocket_friends)

def top_scorer(players):
    return max(players, key=lambda p: p[1])[0]
