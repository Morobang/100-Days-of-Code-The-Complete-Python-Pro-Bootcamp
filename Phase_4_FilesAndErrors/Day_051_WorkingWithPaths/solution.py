# Day 51 Solutions
import os

# Challenge 1
print(os.getcwd())

# Challenge 2
path = os.path.join('Phase_4_FilesAndErrors', 'Day_049_ReadingFiles', 'sample.txt')
print(path)
print(os.path.exists(path))

# Challenge 3
print(os.path.isfile('solution.py'))   # True (this file itself)
print(os.path.isdir(os.getcwd()))      # True (cwd is always a dir)

# Challenge 4
entries = os.listdir('.')
for entry in sorted(entries):
    kind = 'DIR ' if os.path.isdir(entry) else 'FILE'
    print(f'{kind}  {entry}')

# Challenge 5
from pathlib import Path

p = Path('.')
for item in sorted(p.iterdir()):
    print(item.name, '-', 'dir' if item.is_dir() else item.suffix or 'no ext')
