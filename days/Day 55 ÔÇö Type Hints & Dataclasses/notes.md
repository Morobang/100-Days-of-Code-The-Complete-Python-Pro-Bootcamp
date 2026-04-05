# Day 55 — Type Hints & Dataclasses

## Type hints
```python
from typing import List, Dict, Set, Tuple, Optional, Union, Any
from typing import Callable, TypeVar, Generic, Iterator

def fn(x: int, y: str = 'hi') -> Optional[float]: ...

# Common patterns
Optional[T]          # T or None
Union[int, str]      # int or str
List[int]            # list of ints
Dict[str, List[int]] # nested types
Callable[[int], str] # function type
```

## Dataclasses
```python
from dataclasses import dataclass, field

@dataclass
class Foo:
    x: int
    y: str = 'default'
    items: list = field(default_factory=list)  # mutable default

    def __post_init__(self):  # runs after __init__
        if self.x < 0: raise ValueError

@dataclass(frozen=True)   # immutable
@dataclass(order=True)    # enables <, >, ==
```

## Gotchas
- Type hints are NOT enforced at runtime — use mypy for static checking
- Never use `list` or `dict` as default directly — use `field(default_factory=list)`
- `frozen=True` makes the dataclass hashable (usable as dict key)

## Interview tips
- Type hints = self-documenting code that tools can verify
- `Optional[T]` instead of `T | None` for Python < 3.10
- Dataclasses auto-generate `__init__`, `__repr__`, `__eq__`
