# Day 007 — Control Flow

## Key syntax
```python
if condition:
    ...
elif other:
    ...
else:
    ...

# Ternary
x = "yes" if condition else "no"

# Match (Python 3.10+)
match command:
    case "quit": ...
    case "go" | "move": ...
    case _: ...          # default
```

## Gotchas
- Check more specific conditions first — `% 15` before `% 3` and `% 5` in FizzBuzz
- Avoid deeply nested `if` — early returns flatten the code
- `elif` stops checking after the first match — order matters

## Interview tips
- FizzBuzz is literally asked in interviews — know it in 30 seconds flat
- "Replace if-elif chain with a dict" is a common refactor question
- Match/case (structural pattern matching) was added in 3.10 — worth mentioning
