# Day 17 — File I/O — SOLUTIONS
from datetime import datetime

# Exercise 1
games = ['Tekken 8', 'FC26', 'KOF XV', 'Naruto Storm', 'Elden Ring']
with open('/tmp/my_games.txt', 'w') as f:
    for game in games:
        f.write(game + '\n')

with open('/tmp/my_games.txt') as f:
    for i, line in enumerate(f, 1):
        print(f"{i}. {line.strip()}")


# Exercise 2
def count_words_in_file(filepath: str) -> int:
    with open(filepath) as f:
        return sum(len(line.split()) for line in f)


# Exercise 3
def log(message: str, filepath: str):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(filepath, 'a') as f:
        f.write(f'[{timestamp}] {message}\n')
