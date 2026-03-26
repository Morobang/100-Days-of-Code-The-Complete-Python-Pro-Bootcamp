# Day 29 — Linked Lists

## Key patterns
```python
# Traverse
cur = head
while cur:
    print(cur.val)
    cur = cur.next

# Reverse in-place
prev, cur = None, head
while cur:
    nxt = cur.next
    cur.next = prev
    prev, cur = cur, nxt
return prev  # new head

# Slow/fast pointer (cycle, middle)
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
# slow is at middle; if slow==fast → cycle

# Dummy head (simplifies edge cases)
dummy = Node(0); dummy.next = head
cur = dummy
...
return dummy.next
```

## Gotchas
- Always check `if not head` and `if not head.next`
- Dummy head node eliminates head insertion/deletion edge cases
- Slow/fast pointer: fast moves 2x — standard for cycle and middle

## Interview tips
- Reverse linked list — must know by heart
- Has cycle → Floyd's algorithm (no extra space)
- Merge two sorted → dummy head + two pointers
