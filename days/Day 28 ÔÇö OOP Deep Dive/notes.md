# Day 28 — OOP Deep Dive

## Key syntax
```python
@property
def x(self): return self._x

@x.setter
def x(self, val):
    if val<0: raise ValueError
    self._x=val

from abc import ABC, abstractmethod
class Base(ABC):
    @abstractmethod
    def method(self): ...

# Context manager
class MyCtx:
    def __enter__(self): return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        return False  # don't suppress exceptions

# Iterator
class MyIter:
    def __iter__(self): return self
    def __next__(self):
        if done: raise StopIteration
        return next_val
```

## Gotchas
- Properties look like attributes but call methods — great for validation
- `__exit__` returning True suppresses the exception
- Abstract methods MUST be implemented in subclasses

## Interview tips
- Stack/Queue/LRU Cache are classic OOP interview questions
- MinStack: maintain a parallel stack tracking minimums
- LRU Cache: use `OrderedDict` (Python stdlib) or doubly linked list + hash map
