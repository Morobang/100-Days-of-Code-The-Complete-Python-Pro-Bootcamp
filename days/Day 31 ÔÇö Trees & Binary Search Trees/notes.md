# Day 31 — Trees & Binary Search Trees

## Key patterns
```python
# DFS (recursive)
def dfs(node):
    if not node: return
    # preorder: process here
    dfs(node.left)
    # inorder: process here
    dfs(node.right)
    # postorder: process here

# BFS (iterative)
from collections import deque
queue = deque([root])
while queue:
    node = queue.popleft()
    if node.left:  queue.append(node.left)
    if node.right: queue.append(node.right)

# BST insert
def insert(root, val):
    if not root: return TreeNode(val)
    if val < root.val: root.left  = insert(root.left,  val)
    else:              root.right = insert(root.right, val)
    return root
```

## Gotchas
- Always check `if not node: return` first
- Inorder traversal of a BST gives sorted output
- Height = 1 + max(left, right); empty tree = 0

## Interview tips
- Most tree problems: think DFS first, BFS for level-order
- Validate BST: pass min/max bounds down recursively
- LCA in BST: if both < root go left, both > root go right, else root is LCA
