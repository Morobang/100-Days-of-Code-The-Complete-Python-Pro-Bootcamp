# Day 78 — Async Python

## Key patterns
```python
import asyncio

# Run event loop
asyncio.run(main())

# Concurrent tasks
results = await asyncio.gather(coro1(), coro2(), coro3())

# Timeout
try:
    result = await asyncio.wait_for(coro(), timeout=5.0)
except asyncio.TimeoutError: ...

# Queue
q = asyncio.Queue()
await q.put(item)
item = await q.get()

# Semaphore
sem = asyncio.Semaphore(10)
async with sem: await do_work()

# Async generator
async def gen():
    for i in range(10):
        yield i; await asyncio.sleep(0)

async for item in gen(): ...
result = [x async for x in gen()]
```

## Interview tips
- `await` suspends current coroutine until awaitable completes
- `asyncio.gather` runs coroutines concurrently (not parallel — same thread)
- Use `asyncio.Semaphore` to limit concurrent operations
- `async for` / `async with` work with async iterators and context managers
