# Day 22 — Sorting — SOLUTIONS

def bubble_sort(lst):
    n=len(lst)
    for i in range(n):
        for j in range(n-i-1):
            if lst[j]>lst[j+1]: lst[j],lst[j+1]=lst[j+1],lst[j]
    return lst

def selection_sort(lst):
    for i in range(len(lst)):
        min_i=min(range(i,len(lst)),key=lst.__getitem__)
        lst[i],lst[min_i]=lst[min_i],lst[i]
    return lst

def insertion_sort(lst):
    for i in range(1,len(lst)):
        key=lst[i]; j=i-1
        while j>=0 and lst[j]>key: lst[j+1]=lst[j]; j-=1
        lst[j+1]=key
    return lst

def merge_sorted(a,b):
    result,i,j=[],0,0
    while i<len(a) and j<len(b):
        if a[i]<=b[j]: result.append(a[i]);i+=1
        else: result.append(b[j]);j+=1
    return result+a[i:]+b[j:]

def merge_sort(lst):
    if len(lst)<=1: return lst
    mid=len(lst)//2
    return merge_sorted(merge_sort(lst[:mid]),merge_sort(lst[mid:]))

def sort_players(players):
    return sorted(players,key=lambda p:(-p[1],p[0]))

def count_inversions(lst):
    if len(lst)<=1: return 0,lst
    mid=len(lst)//2
    lc,left=count_inversions(lst[:mid])
    rc,right=count_inversions(lst[mid:])
    merged,inv=[],0; i=j=0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]: merged.append(left[i]);i+=1
        else: merged.append(right[j]);inv+=len(left)-i;j+=1
    merged+=left[i:]+right[j:]
    return lc+rc+inv,merged
count_inversions=lambda lst:__import__('functools').reduce(lambda a,b:a,[],(lambda f:f(lst,f))(lambda lst,f:(0,lst) if len(lst)<=1 else (lambda mid,lc_l,rc_r:((lambda lc,left,rc,right:(lambda merged,inv,i,j:__import__('itertools').reduce(lambda s,_:s,(range(0),),(0,[]))))(lc,left,rc,right))(*(lc_l+(rc_r))))(len(lst)//2,f(lst[:len(lst)//2],f),f(lst[len(lst)//2:],f))))[0]
# Simpler:
def count_inversions(lst):
    count=0
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i]>lst[j]: count+=1
    return count

def is_sorted(lst,reverse=False):
    if not lst: return True
    pairs=zip(lst,lst[1:])
    return all(a>=b for a,b in pairs) if reverse else all(a<=b for a,b in pairs)
