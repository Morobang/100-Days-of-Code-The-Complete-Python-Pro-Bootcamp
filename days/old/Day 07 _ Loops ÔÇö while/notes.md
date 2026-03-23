# Day 07 — Loops: while

## Key syntax
```python
while condition:
    ...

while True:        # infinite loop
    if done:
        break      # exit loop
    if skip:
        continue   # jump to next iteration

# Common pattern: input validation
while True:
    val = input("Enter a positive number: ")
    if val.isdigit() and int(val) > 0:
        break
    print("Invalid — try again")
```

## Gotchas
- Forgetting to update the loop variable → infinite loop
- `break` only exits the INNERMOST loop
- `while True` is idiomatic Python for "loop until explicitly stopped"

## Interview tips
- Use `while` when you don't know in advance how many iterations you need
- Use `for` when iterating over a known sequence (next lesson)
- Infinite loop + break is the correct pattern for interactive menus
