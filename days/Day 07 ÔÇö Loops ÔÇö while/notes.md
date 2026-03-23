# Day 07 — Loops: while

## Key syntax
```python
while condition:
    body

while True:       # infinite loop
    if done: break
    if skip: continue

# Common pattern — input validation
while True:
    val = input("Enter a positive number: ")
    if val.isdigit() and int(val) > 0: break
    print("Invalid — try again")
```

## Gotchas
- Missing the update → infinite loop
- `break` exits the INNERMOST loop only
- `continue` skips to the NEXT iteration — code below it doesn't run

## Interview tips
- `while` = unknown number of iterations, `for` = known sequence
- `while True + break` is idiomatic for menus and input validation
