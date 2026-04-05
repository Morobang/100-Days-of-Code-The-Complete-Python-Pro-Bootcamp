# Day 16 — Error Handling

## Key syntax
```python
try:
    risky_code()
except ValueError as e:
    print(e)
except (TypeError, KeyError):
    print("type or key error")
except Exception as e:        # catch-all (use sparingly)
    print(e)
else:
    print("no error occurred")  # runs only if no exception
finally:
    print("always runs")        # cleanup here

# Raise your own
raise ValueError("something went wrong")

# Custom exception
class MyError(Exception):
    pass
```

## Gotchas
- Bare `except:` catches EVERYTHING including KeyboardInterrupt — avoid it
- `except Exception` is safer but still broad — be specific where possible
- `finally` runs even if there's a `return` inside `try` or `except`

## Interview tips
- "What's the difference between else and finally?" — common question
- Custom exceptions make your API self-documenting
- In data engineering, wrap I/O and network calls in try/except — they WILL fail
