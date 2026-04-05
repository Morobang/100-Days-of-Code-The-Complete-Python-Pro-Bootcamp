# Day 45 — Trie

## Key syntax
```python
class TrieNode:
    def __init__(self):
        self.children = {}     # char -> TrieNode
        self.is_end = False    # marks word boundary

# Insert O(m) — m = word length
def insert(self, word):
    node = self.root
    for c in word:
        node = node.children.setdefault(c, TrieNode())
    node.is_end = True

# Search O(m)
def search(self, word):
    node = self.root
    for c in word:
        if c not in node.children: return False
        node = node.children[c]
    return node.is_end

# StartsWith O(m)
def starts_with(self, prefix):
    node = self.root
    for c in prefix:
        if c not in node.children: return False
        node = node.children[c]
    return True
```

## Gotchas
- `is_end` distinguishes "app" from being just a prefix of "apple"
- DFS from prefix node to collect all words with that prefix
- For Word Search II: build Trie of all target words, DFS grid once

## Interview tips
- Trie vs hash map: Trie wins for prefix queries and autocomplete
- Space: O(alphabet_size × max_word_length × num_words)
- Compressed trie (radix tree) saves space for sparse tries
