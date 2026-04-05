# Day 29 — Linked Lists — SOLUTIONS

class Node:
    def __init__(self,val): self.val=val; self.next=None

class LinkedList:
    def __init__(self): self.head=None

    def append(self,val):
        if not self.head: self.head=Node(val); return
        cur=self.head
        while cur.next: cur=cur.next
        cur.next=Node(val)

    def prepend(self,val):
        node=Node(val); node.next=self.head; self.head=node

    def delete(self,val):
        if not self.head: return
        if self.head.val==val: self.head=self.head.next; return
        cur=self.head
        while cur.next:
            if cur.next.val==val: cur.next=cur.next.next; return
            cur=cur.next

    def to_list(self):
        result,cur=[],self.head
        while cur: result.append(cur.val); cur=cur.next
        return result

    def __len__(self):
        count,cur=0,self.head
        while cur: count+=1; cur=cur.next
        return count

    def __str__(self): return '→'.join(str(v) for v in self.to_list())

def reverse_ll(head):
    prev,cur=None,head
    while cur: nxt=cur.next; cur.next=prev; prev,cur=cur,nxt
    return prev

def find_middle(head):
    slow=fast=head
    while fast and fast.next: slow=slow.next; fast=fast.next.next
    return slow.val

def has_cycle(head):
    slow=fast=head
    while fast and fast.next:
        slow=slow.next; fast=fast.next.next
        if slow is fast: return True
    return False

def remove_nth_from_end(head,n):
    dummy=Node(0); dummy.next=head; fast=slow=dummy
    for _ in range(n+1): fast=fast.next
    while fast: slow=slow.next; fast=fast.next
    slow.next=slow.next.next
    return dummy.next

def merge_sorted_ll(l1,l2):
    dummy=Node(0); cur=dummy
    while l1 and l2:
        if l1.val<=l2.val: cur.next=l1; l1=l1.next
        else: cur.next=l2; l2=l2.next
        cur=cur.next
    cur.next=l1 or l2
    return dummy.next
