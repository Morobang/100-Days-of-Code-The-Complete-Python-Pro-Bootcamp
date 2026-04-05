# Day 32 — Stacks, Queues & Deques

## Key patterns
```python
# Stack — use a list
stack = []
stack.append(x)   # push
stack.pop()       # pop
stack[-1]         # peek

# Queue — use deque
from collections import deque
q = deque()
q.append(x)       # enqueue (right)
q.popleft()       # dequeue (left)

# Monotonic stack (daily temps, largest rect)
stack = []
for i, val in enumerate(lst):
    while stack and lst[stack[-1]] < val:
        idx = stack.pop()
        # process idx
    stack.append(i)
```

## Gotchas
- Use `deque` not `list` for queues — `list.pop(0)` is O(n)
- Monotonic stack: process elements as you pop
- `deque` is O(1) at both ends; `list` is O(n) at front

## Interview tips
- Brackets → stack, always
- "Next greater element" → monotonic stack
- Sliding window max → deque (monotonic)
