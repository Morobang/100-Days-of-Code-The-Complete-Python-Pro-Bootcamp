# Day 47 — Tries — SOLUTIONS

class TrieNode:
    def __init__(self): self.children={}; self.is_end=False

class Trie:
    def __init__(self): self.root=TrieNode()

    def insert(self,word):
        node=self.root
        for c in word: node=node.children.setdefault(c,TrieNode())
        node.is_end=True

    def search(self,word):
        node=self.root
        for c in word:
            if c not in node.children: return False
            node=node.children[c]
        return node.is_end

    def starts_with(self,prefix):
        node=self.root
        for c in prefix:
            if c not in node.children: return False
            node=node.children[c]
        return True

    def delete(self,word):
        def helper(node,word,depth):
            if depth==len(word):
                if not node.is_end: return False
                node.is_end=False
                return len(node.children)==0
            c=word[depth]
            if c not in node.children: return False
            should_delete=helper(node.children[c],word,depth+1)
            if should_delete: del node.children[c]; return not node.is_end and len(node.children)==0
            return False
        helper(self.root,word,0)

def longest_common_prefix(words):
    if not words: return ''
    trie=Trie()
    for w in words: trie.insert(w)
    prefix=''; node=trie.root
    while len(node.children)==1 and not node.is_end:
        c=next(iter(node.children)); prefix+=c; node=node.children[c]
    return prefix

def find_words(board,words):
    trie=Trie()
    for w in words: trie.insert(w)
    rows,cols=len(board),len(board[0]); result=set()
    def dfs(r,c,node,path):
        if node.is_end: result.add(path)
        if r<0 or r>=rows or c<0 or c>=cols or board[r][c] not in node.children: return
        tmp=board[r][c]; board[r][c]='#'
        for dr,dc in[(-1,0),(1,0),(0,-1),(0,1)]:
            dfs(r+dr,c+dc,node.children[tmp],path+tmp)
        board[r][c]=tmp
    for r in range(rows):
        for c in range(cols):
            if board[r][c] in trie.root.children: dfs(r,c,trie.root,'')
    return list(result)

def replace_words(dictionary,sentence):
    trie=Trie()
    for w in dictionary: trie.insert(w)
    result=[]
    for word in sentence.split():
        node=trie.root; prefix=''
        for c in word:
            if c not in node.children: prefix=word; break
            prefix+=c; node=node.children[c]
            if node.is_end: break
        result.append(prefix)
    return ' '.join(result)

class MagicDictionary:
    def __init__(self): self.words=[]
    def build(self,words): self.words=words
    def search(self,word):
        for w in self.words:
            if len(w)==len(word) and sum(a!=b for a,b in zip(w,word))==1: return True
        return False
