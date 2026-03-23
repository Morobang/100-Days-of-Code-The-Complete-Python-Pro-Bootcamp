# Day 16 — File I/O — SOLUTIONS
from datetime import datetime

# Write and read
games = ['Tekken 8','FC26','KOF XV','Elden Ring','Naruto Storm']
with open('/tmp/my_games.txt','w') as f:
    for game in games: f.write(game+'\n')

with open('/tmp/my_games.txt') as f:
    for i, line in enumerate(f, 1):
        print(f"{i}. {line.strip()}")

def count_words(filepath):
    with open(filepath) as f:
        return sum(len(line.split()) for line in f)

class Logger:
    def __init__(self, filepath):
        self.filepath = filepath

    def _write(self, level, message):
        ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(self.filepath, 'a') as f:
            f.write(f'[{ts}] {level}: {message}\n')

    def info(self, msg):    self._write('INFO', msg)
    def error(self, msg):   self._write('ERROR', msg)
    def warning(self, msg): self._write('WARNING', msg)
