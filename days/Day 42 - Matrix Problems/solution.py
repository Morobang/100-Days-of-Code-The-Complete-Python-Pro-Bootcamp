# Day 42 — Matrix Problems — SOLUTIONS

def transpose(m):
    return [[m[r][c] for r in range(len(m))] for c in range(len(m[0]))]

def rotate_90(m):
    n=len(m)
    for r in range(n):
        for c in range(r,n): m[r][c],m[c][r]=m[c][r],m[r][c]
    for row in m: row.reverse()

def spiral_order(m):
    result=[]
    while m:
        result+=m.pop(0)
        m=list(map(list,zip(*m)))[::-1]
    return result

def set_zeroes(m):
    rows,cols=set(),set()
    for r in range(len(m)):
        for c in range(len(m[0])):
            if m[r][c]==0: rows.add(r); cols.add(c)
    for r in range(len(m)):
        for c in range(len(m[0])):
            if r in rows or c in cols: m[r][c]=0

def search_matrix(m,target):
    r,c=0,len(m[0])-1
    while r<len(m) and c>=0:
        if m[r][c]==target: return True
        elif m[r][c]>target: c-=1
        else: r+=1
    return False

def diagonal_traverse(m):
    rows,cols=len(m),len(m[0]); result=[]; r=c=0
    for _ in range(rows*cols):
        result.append(m[r][c])
        if (r+c)%2==0:
            if c==cols-1: r+=1
            elif r==0: c+=1
            else: r-=1; c+=1
        else:
            if r==rows-1: c+=1
            elif c==0: r+=1
            else: r+=1; c-=1
    return result

def word_search(board,word):
    rows,cols=len(board),len(board[0])
    def dfs(r,c,i):
        if i==len(word): return True
        if not(0<=r<rows and 0<=c<cols) or board[r][c]!=word[i]: return False
        tmp=board[r][c]; board[r][c]='#'
        found=any(dfs(r+dr,c+dc,i+1) for dr,dc in[(-1,0),(1,0),(0,-1),(0,1)])
        board[r][c]=tmp; return found
    return any(dfs(r,c,0) for r in range(rows) for c in range(cols))

def maximal_square(m):
    if not m: return 0
    rows,cols=len(m),len(m[0]); dp=[[0]*cols for _ in range(rows)]; best=0
    for r in range(rows):
        for c in range(cols):
            if m[r][c]=='1':
                dp[r][c]=1 if r==0 or c==0 else min(dp[r-1][c],dp[r][c-1],dp[r-1][c-1])+1
                best=max(best,dp[r][c])
    return best**2
