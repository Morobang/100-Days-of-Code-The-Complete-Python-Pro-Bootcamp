# Day 45 — Trie — SOLUTIONS

class TrieNode:
    def __init__(self): self.children={}; self.is_end=False

class Trie:
    def __init__(self): self.root=TrieNode()

    def _traverse(self,prefix):
        node=self.root
        for c in prefix:
            if c not in node.children: return None
            node=node.children[c]
        return node

    def insert(self,word):
        node=self.root
        for c in word: node=node.children.setdefault(c,TrieNode())
        node.is_end=True

    def search(self,word):
        node=self._traverse(word)
        return node is not None and node.is_end

    def starts_with(self,prefix):
        return self._traverse(prefix) is not None

    def get_words_with_prefix(self,prefix):
        node=self._traverse(prefix)
        if not node: return []
        results=[]
        def dfs(n,path):
            if n.is_end: results.append(prefix+path)
            for c,child in n.children.items(): dfs(child,path+c)
        dfs(node,''); return results

def find_words(board,words):
    trie=Trie()
    for w in words: trie.insert(w)
    rows,cols=len(board),len(board[0]); found=set()
    def dfs(node,r,c,path):
        ch=board[r][c]
        if ch not in node.children: return
        node=node.children[ch]; path+=ch
        if node.is_end: found.add(path)
        board[r][c]='#'
        for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr,nc=r+dr,c+dc
            if 0<=nr<rows and 0<=nc<cols and board[nr][nc]!='#': dfs(node,nr,nc,path)
        board[r][c]=ch
    for r in range(rows):
        for c in range(cols): dfs(trie.root,r,c,'')
    return list(found)

def replace_words(dictionary,sentence):
    trie=Trie()
    for w in dictionary: trie.insert(w)
    def shortest_root(word):
        node=trie.root
        for i,c in enumerate(word):
            if c not in node.children: return word
            node=node.children[c]
            if node.is_end: return word[:i+1]
        return word
    return ' '.join(shortest_root(w) for w in sentence.split())

def longest_word(words):
    words.sort()
    built=set(['']); result=''
    for w in words:
        if w[:-1] in built:
            built.add(w)
            if len(w)>len(result): result=w
    return result

def count_prefix(words,prefix):
    return sum(1 for w in words if w.startswith(prefix))
