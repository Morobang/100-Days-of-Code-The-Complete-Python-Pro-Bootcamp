# Day 31 — Trees — SOLUTIONS
from collections import deque

class TreeNode:
    def __init__(self,val): self.val=val; self.left=self.right=None

def insert(root,val):
    if not root: return TreeNode(val)
    if val<root.val: root.left=insert(root.left,val)
    else: root.right=insert(root.right,val)
    return root

def search(root,val):
    if not root: return False
    if root.val==val: return True
    return search(root.left,val) if val<root.val else search(root.right,val)

def inorder(root):
    return [] if not root else inorder(root.left)+[root.val]+inorder(root.right)

def preorder(root):
    return [] if not root else [root.val]+preorder(root.left)+preorder(root.right)

def postorder(root):
    return [] if not root else postorder(root.left)+postorder(root.right)+[root.val]

def max_depth(root):
    return 0 if not root else 1+max(max_depth(root.left),max_depth(root.right))

def is_balanced(root):
    def height(node):
        if not node: return 0
        l,r=height(node.left),height(node.right)
        if l<0 or r<0 or abs(l-r)>1: return -1
        return 1+max(l,r)
    return height(root)>=0

def level_order(root):
    if not root: return []
    q,result=deque([root]),[]
    while q:
        level=[]; q2=deque()
        while q: n=q.popleft(); level.append(n.val); (q2.append(n.left) if n.left else None); (q2.append(n.right) if n.right else None)
        result.append(level); q=q2
    return result

def lca(root,p,q):
    if p<root.val and q<root.val: return lca(root.left,p,q)
    if p>root.val and q>root.val: return lca(root.right,p,q)
    return root.val

def is_valid_bst(root,lo=float('-inf'),hi=float('inf')):
    if not root: return True
    if not (lo<root.val<hi): return False
    return is_valid_bst(root.left,lo,root.val) and is_valid_bst(root.right,root.val,hi)

def right_side_view(root):
    if not root: return []
    result=[]; q=deque([root])
    while q:
        for _ in range(len(q)-1): node=q.popleft(); (q.append(node.left) if node.left else None); (q.append(node.right) if node.right else None)
        node=q.popleft(); result.append(node.val)
        (q.append(node.left) if node.left else None); (q.append(node.right) if node.right else None)
    return result
