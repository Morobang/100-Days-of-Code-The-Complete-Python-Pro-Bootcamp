# Day 52 — Functional Programming

## Key tools
```python
from functools import reduce, partial, lru_cache, wraps
from itertools import chain, islice, groupby, product, combinations

reduce(fn, iterable, initial)     # fold
partial(fn, *args)                # pre-fill args
lru_cache(maxsize=None)           # memoize decorator

chain(a, b, c)                    # merge iterables
islice(iterable, stop)            # lazy slice
groupby(iterable, key=fn)         # group consecutive
product(a, b)                     # cartesian product
combinations(iterable, r)         # C(n,r)
permutations(iterable, r)         # P(n,r)
```

## Functional principles
- **Pure functions**: same input always gives same output, no side effects
- **Immutability**: don't modify inputs
- **Composition**: build complex from simple
- **Point-free**: define functions without mentioning arguments

## Interview tips
- `reduce` can implement map and filter
- `partial` pre-fills — useful for callbacks and configuration
- Generators are lazy functional pipelines
