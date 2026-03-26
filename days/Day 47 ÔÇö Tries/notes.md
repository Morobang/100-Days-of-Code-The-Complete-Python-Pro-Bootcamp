# Day 47 — Tries

## Structure
```python
class TrieNode:
    def __init__(self):
        self.children = {}   # char → TrieNode
        self.is_end = False
        self.count = 0       # optional: words passing through

# Insert: walk chars, create nodes, mark end
# Search: walk chars, return is_end
# Prefix: walk chars, return True if all found
# Delete: recursive — remove nodes with no children
```

## Common patterns
```python
# Autocomplete: DFS from prefix endpoint
def autocomplete(prefix):
    node = navigate_to(prefix)
    results = []
    dfs(node, prefix, results)
    return results

# Replace with root: insert all roots, then for each word
# walk trie until is_end or word exhausted
```

## Gotchas
- `is_end` marks a complete word — separate from having children
- Delete: only remove nodes if they have no other children
- For board + words: build Trie of words, DFS on board

## Interview tips
- "Prefix search" → Trie, always
- "Autocomplete" → Trie + DFS from prefix node
- Word Search II: Trie is essential — O(M × 4^L) without, much faster with
