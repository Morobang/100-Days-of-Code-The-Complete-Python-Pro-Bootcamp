# Day 3 — Quick Reference

## Creating strings

```python
single = 'Hello'
double = "Hello"          # same thing — use whichever you prefer
apostrophe = "It's fine"  # use double quotes if the string has an apostrophe
quote = 'He said "hi"'    # use single quotes if the string has double quotes
```

## len()

```python
len("Python")    # 6
len("")          # 0
len("  hi  ")   # 6 (spaces count)
```

## Indexing

```python
word = "Python"
word[0]   # "P"  — first character (index starts at 0)
word[1]   # "y"
word[-1]  # "n"  — last character
word[-2]  # "o"  — second to last
```

## Concatenation (joining)

```python
first = "Hello"
second = "World"
result = first + ", " + second + "!"   # "Hello, World!"
```

## Repetition

```python
"ha" * 3        # "hahaha"
"-" * 30        # "------------------------------"
```

## Gotchas

- Index starts at 0, not 1. The first character is `[0]`.
- Negative indexes work backwards: `[-1]` is the last character.
- Accessing an index that doesn't exist causes an `IndexError`. If a string has 5 characters, valid indexes are 0–4 (and -1 to -5).
- You cannot concatenate a string and a number directly: `"Age: " + 25` will error. Use `str(25)` first (full lesson Day 8).
