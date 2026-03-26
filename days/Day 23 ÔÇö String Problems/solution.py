# Day 23 — String Problems — SOLUTIONS

def reverse_words(s): return ' '.join(s.split()[::-1])

def is_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

def is_anagram(s,t): return sorted(s)==sorted(t)

def first_unique(s):
    from collections import Counter
    freq=Counter(s)
    return next((c for c in s if freq[c]==1),'')

def longest_common_prefix(words):
    if not words: return ''
    prefix=words[0]
    for w in words[1:]:
        while not w.startswith(prefix): prefix=prefix[:-1]
        if not prefix: return ''
    return prefix

def is_valid_brackets(s):
    stack=[]; pairs={')':'(',']':'[','}':'{'}
    for c in s:
        if c in '([{': stack.append(c)
        elif c in ')]}':
            if not stack or stack[-1]!=pairs[c]: return False
            stack.pop()
    return not stack

def longest_unique_substring(s):
    seen={}; left=max_len=0
    for right,c in enumerate(s):
        if c in seen and seen[c]>=left: left=seen[c]+1
        seen[c]=right; max_len=max(max_len,right-left+1)
    return max_len

def group_anagrams(words):
    groups={}
    for w in words:
        key=tuple(sorted(w)); groups.setdefault(key,[]).append(w)
    return list(groups.values())

def is_rotation(s,t): return len(s)==len(t) and t in s+s
