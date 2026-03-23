# Day 16 — File I/O

## Key syntax
```python
with open('file.txt', 'w') as f:
    f.write('text\n')
    f.writelines(['a\n','b\n'])

with open('file.txt') as f:     # 'r' is default
    content = f.read()          # whole file
    lines   = f.readlines()     # list with \n
    line    = f.readline()      # one line

for line in f:                  # memory efficient
    print(line.strip())

# Modes: 'r' 'w' 'a' 'r+' 'rb' 'wb'
```

## Gotchas
- Always use `with` — closes the file automatically
- `readlines()` keeps `\n` — use `.strip()`
- `'w'` OVERWRITES — use `'a'` to append
- Large files: loop line-by-line, never `read()` all at once

## Interview tips
- `with` = context manager protocol (`__enter__`/`__exit__`)
- For large files, iterate line by line — never `read()` a 10GB file
- `pathlib.Path` is the modern way to handle file paths
