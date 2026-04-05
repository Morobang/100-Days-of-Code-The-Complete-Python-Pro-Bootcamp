# Day 56 — Context Managers & Protocols

## Context manager
```python
# Class-based
class CM:
    def __enter__(self): return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        # cleanup
        return False  # don't suppress exceptions

# contextmanager decorator
from contextlib import contextmanager
@contextmanager
def cm():
    # setup
    try:
        yield resource
    finally:
        # cleanup (always runs)
        pass
```

## Key protocols
| Protocol | Methods needed |
|----------|---------------|
| Iterable | `__iter__` |
| Iterator | `__iter__`, `__next__` |
| Sequence | `__len__`, `__getitem__` |
| Mapping | `__getitem__`, `__setitem__`, `__len__`, `__iter__` |
| Context Manager | `__enter__`, `__exit__` |

## Gotchas
- `__exit__` returning True suppresses exceptions — usually return False
- `finally` in contextmanager always runs — even if exception
- Implement `__iter__` and `__len__` to make `in` work on custom containers

## Interview tips
- Context managers → resource management (DB connections, file handles, locks)
- Duck typing: if it has `__iter__`, it's iterable — no base class needed
- `__contains__` for O(1) membership if using hash-based storage
