# Day 50 — Algorithm Visualiser — SOLUTIONS

def bubble_sort_steps(lst):
    lst=lst[:]; n=len(lst); cmps=0
    for i in range(n):
        for j in range(n-i-1):
            cmps+=1; yield lst[:],(j,j+1)
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]; yield lst[:],(j,j+1)
    yield lst[:],()

def insertion_sort_steps(lst):
    lst=lst[:]
    for i in range(1,len(lst)):
        key=lst[i]; j=i-1
        while j>=0 and lst[j]>key:
            yield lst[:],(j,j+1)
            lst[j+1]=lst[j]; j-=1
        lst[j+1]=key; yield lst[:],()
    yield lst[:],()

def render(state,highlighted=()):
    nums=' '.join(f'{n:3}' for n in state)
    markers=''.join('  ^ ' if i in highlighted else '    ' for i in range(len(state)))
    print(f'[{nums}]')
    if highlighted: print(f' {markers}')

def run_with_stats(algo_steps,lst):
    steps=cmps=0; last=lst[:]
    for state,hi in algo_steps(lst):
        steps+=1; last=state
        if hi: cmps+=1
    return last,steps,cmps

def merge_sort_steps(lst):
    lst=lst[:]
    def merge_sort(l):
        if len(l)<=1: return l
        mid=len(l)//2
        left=merge_sort(l[:mid]); right=merge_sort(l[mid:])
        return merge(left,right)
    def merge(a,b):
        result=[]; i=j=0
        while i<len(a) and j<len(b):
            if a[i]<=b[j]: result.append(a[i]); i+=1
            else: result.append(b[j]); j+=1
        return result+a[i:]+b[j:]
    yield merge_sort(lst),()

def compare_sorts(lst):
    algos=[('Bubble Sort',bubble_sort_steps),('Insertion Sort',insertion_sort_steps),('Merge Sort',merge_sort_steps)]
    print(f"{'Algorithm':<20} {'Steps':>8} {'Comparisons':>12}")
    print('-'*42)
    for name,algo in algos:
        _,steps,cmps=run_with_stats(algo,lst)
        print(f"{name:<20} {steps:>8} {cmps:>12}")
