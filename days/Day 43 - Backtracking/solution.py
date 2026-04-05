# Day 43 — Backtracking — SOLUTIONS

def permutations(nums):
    result=[]
    def bt(path,rem):
        if not rem: result.append(path[:]); return
        for i in range(len(rem)):
            path.append(rem[i]); bt(path,rem[:i]+rem[i+1:]); path.pop()
    bt([],nums); return result

def combinations(n,k):
    result=[]
    def bt(start,path):
        if len(path)==k: result.append(path[:]); return
        for i in range(start,n+1):
            path.append(i); bt(i+1,path); path.pop()
    bt(1,[]); return result

def subsets(nums):
    result=[]
    def bt(i,path):
        result.append(path[:])
        for j in range(i,len(nums)):
            path.append(nums[j]); bt(j+1,path); path.pop()
    bt(0,[]); return result

def combination_sum(candidates,target):
    result=[]; candidates.sort()
    def bt(start,path,rem):
        if rem==0: result.append(path[:]); return
        for i in range(start,len(candidates)):
            if candidates[i]>rem: break
            path.append(candidates[i]); bt(i,path,rem-candidates[i]); path.pop()
    bt(0,[],target); return result

def letter_combos(digits):
    if not digits: return []
    phone={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
    result=[]
    def bt(i,path):
        if i==len(digits): result.append(path); return
        for c in phone[digits[i]]: bt(i+1,path+c)
    bt(0,''); return result

def gen_parens(n):
    result=[]
    def bt(path,op,cl):
        if len(path)==2*n: result.append(path); return
        if op<n: bt(path+'(',op+1,cl)
        if cl<op: bt(path+')',op,cl+1)
    bt('',0,0); return result

def n_queens(n):
    count=[0]; cols=set(); d1=set(); d2=set()
    def bt(r):
        if r==n: count[0]+=1; return
        for c in range(n):
            if c in cols or (r-c) in d1 or (r+c) in d2: continue
            cols.add(c); d1.add(r-c); d2.add(r+c)
            bt(r+1)
            cols.remove(c); d1.remove(r-c); d2.remove(r+c)
    bt(0); return count[0]

def solve_sudoku(board):
    def is_valid(r,c,d):
        if d in board[r]: return False
        if any(board[i][c]==d for i in range(9)): return False
        br,bc=3*(r//3),3*(c//3)
        return not any(board[br+i][bc+j]==d for i in range(3) for j in range(3))
    def bt():
        for r in range(9):
            for c in range(9):
                if board[r][c]=='.':
                    for d in '123456789':
                        if is_valid(r,c,d):
                            board[r][c]=d
                            if bt(): return True
                            board[r][c]='.'
                    return False
        return True
    return bt()

def palindrome_partition(s):
    result=[]
    def is_pal(t): return t==t[::-1]
    def bt(start,path):
        if start==len(s): result.append(path[:]); return
        for end in range(start+1,len(s)+1):
            if is_pal(s[start:end]):
                path.append(s[start:end]); bt(end,path); path.pop()
    bt(0,[]); return result
