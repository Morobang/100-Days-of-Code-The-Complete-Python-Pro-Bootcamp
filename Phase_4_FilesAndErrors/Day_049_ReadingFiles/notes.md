# Reading Files — Quick Reference

## Always Use `with`
The `with` statement automatically closes the file when the block exits — even if an error occurs.
```python
with open('file.txt', 'r', encoding='utf-8') as f:
    contents = f.read()
# file is closed here automatically
```

## Reading Methods
| Method | Returns | Best when |
|--------|---------|-----------|
| `.read()` | Entire file as one string | File is small, need all text |
| `.readlines()` | List of lines (each includes `\n`) | Need random access by index |
| `.readline()` | Next single line | Manual line-by-line control |
| `for line in f:` | One line per iteration | Most common — memory-efficient |

## Common Patterns
```python
# Full text as a string
with open('file.txt', encoding='utf-8') as f:
    text = f.read()

# List of clean lines (no trailing \n)
with open('file.txt', encoding='utf-8') as f:
    lines = [line.strip() for line in f]

# Count lines
with open('file.txt', encoding='utf-8') as f:
    count = sum(1 for _ in f)

# Process line by line
with open('file.txt', encoding='utf-8') as f:
    for line in f:
        print(line.strip())
```

## File Modes
| Mode | Meaning |
|------|---------|
| `'r'` | Read (default) — file must exist |
| `'w'` | Write — creates or **overwrites** |
| `'a'` | Append — adds to end |
| `'x'` | Create — fails if file already exists |

## Encoding
Always pass `encoding='utf-8'` to avoid platform-specific surprises.
