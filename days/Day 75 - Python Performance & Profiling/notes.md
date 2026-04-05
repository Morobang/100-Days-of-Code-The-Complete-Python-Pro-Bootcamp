# Day 75 — Python Performance

## Timing code
```python
import timeit
timeit.timeit('code', globals=globals(), number=10000)

import time
start = time.perf_counter()
do_work()
elapsed = time.perf_counter() - start
```

## Profiling
```python
import cProfile
cProfile.run('my_function()')

# Or as decorator
import functools, cProfile
def profile(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        result = fn(*args, **kwargs)
        pr.disable()
        pr.print_stats(sort='cumulative')
        return result
    return wrapper
```

## Common speedups
| Slow | Fast | Why |
|------|------|-----|
| `x in list` | `x in set` | O(n) → O(1) |
| `list.count()` in loop | `Counter(list)` | O(n²) → O(n) |
| Nested loops | NumPy vectorisation | Interpreted → C |
| Large class instances | `__slots__` | Reduce dict overhead |
| Recursive fib | `lru_cache` | Memoize subproblems |
| `list` of results | Generator | Lazy — no memory upfront |

## Interview tips
- Know Big O but also constant factors (hash tables have overhead)
- Profile first, optimise second — don't guess at bottlenecks
- `sys.getsizeof` gives shallow size — use `tracemalloc` for deep size
