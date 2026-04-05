# Day 49 — Easy Problems — SOLUTIONS
from collections import Counter

def two_sum(lst,target):
    seen={}
    for i,x in enumerate(lst):
        if target-x in seen: return (seen[target-x],i)
        seen[x]=i

def is_anagram(s,t): return Counter(s)==Counter(t)
def has_duplicate(lst): return len(lst)!=len(set(lst))

def max_profit(prices):
    min_p=float('inf'); best=0
    for p in prices: min_p=min(min_p,p); best=max(best,p-min_p)
    return best

class Node:
    def __init__(self,v): self.val=v; self.next=None

def is_palindrome_list(head):
    vals=[]
    while head: vals.append(head.val); head=head.next
    return vals==vals[::-1]

def merge_sorted(nums1,m,nums2,n):
    i,j,k=m-1,n-1,m+n-1
    while i>=0 and j>=0:
        if nums1[i]>nums2[j]: nums1[k]=nums1[i]; i-=1
        else: nums1[k]=nums2[j]; j-=1
        k-=1
    while j>=0: nums1[k]=nums2[j]; j-=1; k-=1

def climb_stairs(n):
    a,b=1,1
    for _ in range(n-1): a,b=b,a+b
    return b

def reverse_list(head):
    prev,cur=None,head
    while cur: nxt=cur.next; cur.next=prev; prev,cur=cur,nxt
    return prev

def is_balanced(s):
    stack=[]; pairs={')':'(',']':'[','}':'{'}
    for c in s:
        if c in '([{': stack.append(c)
        elif c in ')]}':
            if not stack or stack[-1]!=pairs[c]: return False
            stack.pop()
    return not stack

def max_depth(root):
    return 0 if not root else 1+max(max_depth(root.left),max_depth(root.right))

def move_zeros(lst):
    k=0
    for i in range(len(lst)):
        if lst[i]!=0: lst[k]=lst[i]; k+=1
    for i in range(k,len(lst)): lst[i]=0

def intersect(a,b):
    ca=Counter(a)
    return [x for x in b if ca[x]>0 and (ca.__setitem__(x,ca[x]-1) or True)]
