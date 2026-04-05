# Day 74 — System Design Concepts

## Core building blocks to know
| Component | Python implementation |
|-----------|----------------------|
| LRU Cache | `OrderedDict` + `move_to_end` |
| Rate limiter | Token bucket or sliding window |
| Message queue | `deque` or `queue.Queue` |
| Pub/Sub | `dict` of subscriber lists |
| Consistent hash | Sorted hash ring |

## Rate limiter algorithms
```
Token bucket:   tokens refill at rate R, cap at C
                allow if tokens >= 1, deduct 1
Sliding window: track request timestamps in a deque
                allow if count in last window_seconds < max_requests
Fixed window:   count per time period (simpler, less fair)
```

## CAP theorem (know for interviews)
- Consistency: all nodes see same data at same time
- Availability: every request gets a response
- Partition tolerance: system continues despite network splits
- **Can only guarantee 2 of 3**

## Interview tips
- "Design a cache" → LRU with OrderedDict or doubly linked list + hash map
- "Design a rate limiter" → token bucket for burst tolerance
- "Design a URL shortener" → hash function + DB + redirect
- Always discuss trade-offs: consistency vs availability
