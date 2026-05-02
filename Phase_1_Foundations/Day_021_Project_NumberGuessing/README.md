# Day 21 — Project: Number Guessing Game

Your first project that uses Python's standard library. The computer picks a secret number between 1 and 100 — you have to guess it.

## New concept for today

```python
import random
secret = random.randint(1, 100)   # random integer from 1 to 100 inclusive
```

`import random` loads Python's built-in random module. You will learn more about modules and imports on Day 35.

## Requirements

Your program must:

1. Pick a random number between 1 and 100
2. Ask the user to guess
3. After each wrong guess, print `Too high!` or `Too low!`
4. When the user guesses correctly, print a congratulations message and the number of attempts
5. Ask if the user wants to play again

## Sample output

```
Guess a number between 1 and 100: 50
Too high! Try again.
Guess again: 25
Too low! Try again.
Guess again: 37
Too high! Try again.
Guess again: 31
Correct! The number was 31. You got it in 4 guess(es).

Play again? (yes/no): yes
Guess a number between 1 and 100: ...
```

## Files

| File | Purpose |
|------|---------|
| `starter.py` | Start here — skeleton with hints |
| `solution/number_guessing.py` | Check after you've tried |

## Concepts used

- `import random` + `random.randint()` — new today
- `while` loops (Day 13) — outer loop for play-again, inner for guessing
- `if / elif / else` (Day 12) — high / low / correct logic
- `int(input())` (Day 8) — getting the guess
- f-strings (Day 10) — formatted output
- A counter variable (Day 13) — tracking attempts

## Stretch goals

- Limit the player to 10 guesses (if they run out, reveal the number)
- Track the player's best score across multiple rounds
- Add difficulty levels: Easy (1–50), Medium (1–100), Hard (1–500)
