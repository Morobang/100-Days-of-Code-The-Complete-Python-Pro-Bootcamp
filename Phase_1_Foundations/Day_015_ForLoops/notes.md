# Day 15 — Quick Reference

## Basic for loop

```python
for item in sequence:
    # runs once for each item in sequence
```

## Iterating over a string

```python
for char in 'hello':
    print(char)    # h, e, l, l, o  (one per line)
```

## range()

```python
range(5)           # 0, 1, 2, 3, 4          — stop only
range(1, 6)        # 1, 2, 3, 4, 5          — start and stop
range(0, 10, 2)    # 0, 2, 4, 6, 8          — start, stop, step
range(10, 0, -1)   # 10, 9, 8, ..., 1       — count down
```

```python
for i in range(1, 6):
    print(i)    # 1, 2, 3, 4, 5
```

## break and continue

```python
for i in range(10):
    if i == 5:
        break       # stop the loop entirely at 5
    print(i)        # 0, 1, 2, 3, 4

for i in range(10):
    if i % 2 == 0:
        continue    # skip even numbers
    print(i)        # 1, 3, 5, 7, 9
```

## enumerate()

```python
for i, char in enumerate('abc'):
    print(i, char)    # 0 a / 1 b / 2 c

for i, char in enumerate('abc', start=1):
    print(i, char)    # 1 a / 2 b / 3 c
```

## Gotchas

- `range(stop)` starts at 0 and goes up to (not including) `stop`.
- `range(1, 11)` gives 1 through 10 — the stop is exclusive.
- The loop variable (`i`, `char`, etc.) is just a name you choose — pick something meaningful.
- Unlike `while`, you don't need to update the variable yourself — `for` does it automatically.
