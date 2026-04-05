# Day 53 — Concurrency Basics

## When to use what
```
threading     → I/O-bound: network, files, DB queries
               Uses GIL — limited CPU parallelism
multiprocessing → CPU-bound: number crunching, image processing
               Bypasses GIL — true parallelism
asyncio       → High-concurrency I/O (thousands of connections)
               Single thread — no GIL issues, no context switching
```

## Key APIs
```python
# Threading
import threading
t = threading.Thread(target=fn, args=())
t.start(); t.join()
lock = threading.Lock()
with lock: ...  # thread-safe section

# Executor pools
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
with ThreadPoolExecutor(max_workers=4) as ex:
    results = list(ex.map(fn, items))

# asyncio
async def fn(): await asyncio.sleep(1)
results = await asyncio.gather(fn1(), fn2())
sem = asyncio.Semaphore(10)
async with sem: ...
```

## Gotchas
- `threading` with CPU-bound code is often SLOWER than single-thread (GIL)
- Always use `Lock` for shared mutable state in threads
- `asyncio` functions must be called with `await` — forgetting = no execution

## Interview tips
- GIL → threads share memory but can't truly run Python in parallel (CPU-bound)
- `Queue` is the safe way to pass data between threads/processes
- async/await is cooperative multitasking — only one coroutine runs at a time
