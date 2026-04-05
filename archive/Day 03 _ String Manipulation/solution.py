# Day 03 — String Manipulation — SOLUTIONS

# Exercise 1 — title case without .title()
name = "rocket tshigidimisa"
# Split into words, capitalise first letter of each, rejoin
words = name.split()
titled = " ".join(word[0].upper() + word[1:] for word in words)
print(titled)   # → Rocket Tshigidimisa

# Exercise 2 — f-string
player = "Rocket"
game = "Tekken 8"
score = 9500
print(f"Player: {player} | Game: {game} | Score: {score}")

# Exercise 3 — initials
def initials(full_name: str) -> str:
    # Split name into parts, grab first char of each, join with "."
    parts = full_name.split()
    return ".".join(part[0].upper() for part in parts)
