# Day 23 — String Problems

## Key techniques
```python
# Two pointers
left, right = 0, len(s)-1
while left < right: ...

# Sliding window
window = set(); left = 0
for right in range(len(s)):
    while s[right] in window:
        window.remove(s[left]); left+=1
    window.add(s[right])

# Character frequency
from collections import Counter
Counter('hello')  # {'l':2,'h':1,'e':1,'o':1}

# Stack for brackets
stack = []
for ch in s:
    if ch in '([{': stack.append(ch)
    elif stack and matches(stack[-1],ch): stack.pop()
    else: return False
return not stack
```

## Gotchas
- Always consider empty string and single char cases
- `s.strip()` then `s.split()` for cleaning whitespace in word problems
- Sorting is O(n log n) — frequency dict is O(n) for anagram

## Interview tips
- Palindrome: two-pointer from both ends
- Anagram: sort both OR compare Counter dicts
- Sliding window: O(n) instead of O(n²) for substring problems
