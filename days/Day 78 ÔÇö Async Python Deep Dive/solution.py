# Day 78 — Async Python — SOLUTIONS
import asyncio

async def async_range(start,stop,step=1):
    i=start
    while i<stop: yield i; i+=step

async def async_map(fn,aiterable):
    result=[]
    async for item in aiterable: result.append(fn(item))
    return result

async def async_filter(pred,aiterable):
    result=[]
    async for item in aiterable:
        if pred(item): result.append(item)
    return result

async def pipeline(numbers):
    q_in=asyncio.Queue(); q_out=asyncio.Queue()
    async def producer():
        for n in numbers: await q_in.put(n)
        await q_in.put(None)
    async def worker():
        while True:
            n=await q_in.get()
            if n is None: await q_out.put(None); break
            await q_out.put(n**2)
    async def collector():
        results=[]
        while True:
            v=await q_out.get()
            if v is None: break
            results.append(v)
        return results
    _,_,result=await asyncio.gather(producer(),worker(),collector())
    return result

async def with_timeout(coro,seconds):
    return await asyncio.wait_for(coro,timeout=seconds)

async def safe_gather(*coros):
    results=[]
    for coro in coros:
        try: results.append((await coro,None))
        except Exception as e: results.append((None,e))
    return results
