# Day 49 — Advanced Sorting & Searching

## Non-comparison sorts
| Algorithm | Time | Space | When |
|-----------|------|-------|------|
| Counting | O(n+k) | O(k) | Small integer range |
| Radix | O(d·n) | O(n) | Fixed-digit integers |
| Bucket | O(n) avg | O(n) | Uniform distribution |

## Quickselect
```python
def quickselect(lst, k):
    pivot = random.choice(lst)
    low  = [x for x in lst if x < pivot]
    mid  = [x for x in lst if x == pivot]
    high = [x for x in lst if x > pivot]
    if k < len(low): return quickselect(low, k)
    elif k < len(low+mid): return pivot
    else: return quickselect(high, k-len(low)-len(mid))
```

## Dutch national flag (3-way partition)
```python
lo=mid=0; hi=len(lst)-1
while mid<=hi:
    if lst[mid]==0: lst[lo],lst[mid]=lst[mid],lst[lo]; lo+=1; mid+=1
    elif lst[mid]==1: mid+=1
    else: lst[mid],lst[hi]=lst[hi],lst[mid]; hi-=1
```

## Interview tips
- "Find kth largest/smallest" → quickselect O(n) average
- "Sort with only 3 values" → Dutch national flag
- "Kth largest in stream" → min-heap of size k
