# Day 17 — File I/O

## Key syntax
```python
# Writing
with open('file.txt', 'w') as f:
    f.write('text\n')
    f.writelines(['line1\n', 'line2\n'])

# Reading
with open('file.txt', 'r') as f:
    content = f.read()          # whole file as string
    lines   = f.readlines()     # list of lines (with \n)
    line    = f.readline()      # one line at a time

# Loop line by line (memory efficient)
with open('file.txt') as f:
    for line in f:
        print(line.strip())

# Modes
'r'   # read (default)
'w'   # write — creates/overwrites
'a'   # append
'rb'  # read binary
'wb'  # write binary
```

## Gotchas
- Always use `with` — it closes the file automatically even if an error occurs
- `readlines()` keeps `\n` at end of each line — use `.strip()` to remove
- `'w'` mode **overwrites** the file — use `'a'` to append
- `f.read()` on a large file loads it all into memory — loop line by line for big files

## Interview tips
- `with` statement = context manager — know how it works
- For large files, iterate line by line — never `read()` a 10GB file
- In data engineering, files are everywhere — S3 objects, local CSVs, logs
