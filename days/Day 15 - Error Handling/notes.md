# Day 15 — Error Handling

## Key syntax
```python
try:
    risky()
except ValueError as e:
    print(e)
except (TypeError, KeyError):
    ...
except Exception as e:        # broad catch-all
    ...
else:
    print("no error")         # only if no exception
finally:
    print("always runs")      # cleanup

raise ValueError("message")   # raise an exception

class MyError(Exception):      # custom exception
    pass
```

## Gotchas
- Bare `except:` catches EVERYTHING including Ctrl+C — avoid it
- `finally` runs even if there's a `return` inside try/except
- Don't use exceptions for normal flow control

## Interview tips
- Wrap I/O and network calls in try/except — they WILL fail
- Custom exceptions make your API self-documenting
- "What's the difference between else and finally?" — common question
