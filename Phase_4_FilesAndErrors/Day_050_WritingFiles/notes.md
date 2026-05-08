# Writing Files — Quick Reference

## Write Mode `'w'`
Creates the file if it does not exist. **Overwrites** the entire file if it does exist.
```python
with open('output.txt', 'w', encoding='utf-8') as f:
    f.write('Hello, file!\n')
```

## Append Mode `'a'`
Creates the file if it does not exist. Adds content to the **end** if it does exist.
```python
with open('log.txt', 'a', encoding='utf-8') as f:
    f.write('New entry\n')
```

## `.write()` vs `.writelines()`
```python
# .write() — one string at a time, no automatic newline
with open('out.txt', 'w', encoding='utf-8') as f:
    f.write('line one\n')
    f.write('line two\n')

# .writelines() — iterable of strings, still no automatic newlines
lines = ['line one\n', 'line two\n', 'line three\n']
with open('out.txt', 'w', encoding='utf-8') as f:
    f.writelines(lines)
```

## Write Then Read Back
```python
# Write
with open('data.txt', 'w', encoding='utf-8') as f:
    f.write('hello\n')

# Read
with open('data.txt', 'r', encoding='utf-8') as f:
    print(f.read())
```

## Mode Summary
| Mode | File exists | File absent |
|------|------------|-------------|
| `'r'` | Read from start | `FileNotFoundError` |
| `'w'` | Overwrite | Create new |
| `'a'` | Append to end | Create new |
| `'x'` | `FileExistsError` | Create new |
