
from bisect import bisect_left
n,m=map(int,input().split())
a=set(map(int,input().split()))
ans=[0]
"""
next=0
for i in range(1,n+1):
    next=bisect_left(a,i)
    print(a[next]-i)
"""
for i in range(n-1,0,-1):
    if i in a:
        ans.append(0)
    else:
        ans.append(ans[-1]+1)
for i in range(n):
    print(ans[-1-i])