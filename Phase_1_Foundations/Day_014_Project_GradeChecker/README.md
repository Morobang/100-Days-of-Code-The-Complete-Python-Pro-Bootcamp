# Day 14 — Project: Grade Checker

Your first real project using conditionals. This program takes a student's name and score, validates the input, calculates a letter grade, and prints a formatted result card.

## Requirements

Your program must:

1. Ask for the student's name
2. Ask for a score between 0 and 100
3. **Validate** the score — if it's outside 0–100, keep asking until it's valid
4. Calculate the letter grade:
   - **A** — 90 and above
   - **B** — 80 to 89
   - **C** — 70 to 79
   - **D** — 60 to 69
   - **F** — below 60
5. Determine **Pass** (60+) or **Fail** (below 60)
6. Print a formatted result card

## Sample output

```
Enter student name: alice
Enter score (0-100): 150
Score must be between 0 and 100. Try again.
Enter score (0-100): 84

==============================
  Student: Alice
  Score:   84/100
  Grade:   B
  Result:  Pass
==============================
```

## Files

| File | Purpose |
|------|---------|
| `starter.py` | Start here — skeleton with hints |
| `solution/grade_checker.py` | Check after you've tried |

## Concepts used

- `input()` and type conversion (Days 6, 8)
- `while` loop for input validation (Day 13)
- `if / elif / else` for grade logic (Day 12)
- f-strings and alignment (Day 10)
- `.strip().title()` for name formatting (Day 9)

## Stretch goals

- Also print the average of multiple students (keep asking for more names/scores until the user types `done`)
- Add a percentage display: `84%`
- Print a progress bar: `########  ` for 84%
