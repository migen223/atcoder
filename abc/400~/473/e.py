import sys

from collections import defaultdict,deque
from bisect import bisect_right
def debug(*x):print('debug:',*x, file=sys.stderr)
sys.setrecursionlimit(300000)
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
mmi= lambda: map(lambda x:int (x)-1, input().split())
li = lambda: list(mi())
inf = 2 ** 61 - 1
mod = 998244353
#mod=10**9+7
dy=[-1,1,0,0]
dx=[0,0,-1,1]
#dy=[-1,-1,-1,1,1,1,0,0]
#dx=[-1,0,1,-1,0,1,-1,1]

n,k=mi()
a=li()
r=[0]
d=defaultdict(deque)
d[0].append(0)
for i in range(1,1+n):
    ri=(r[-1]+a[i-1])%k
    r.append(ri)
    d[ri].append(i)
for di in d:
    d[di].append(inf)

#print(d)
right=inf
ans=0
for i in range(n+1):
    #debug(r[i],right)
    d[r[i]].popleft()
    if a[i-1]%k==0 and i>=1:
        ans+=1
        right=inf
    next=d[r[i]][0]
    if right==i:
        ans+=1  
        right=inf
    if next<right:
        right=next

print(ans)
"""
r=[a[0]%k]
d=defaultdict(list)
d[a[0]%k].append(0)
for i in range(1,n):
    ri=(r[-1]+a[i])%k
    r.append(ri)
    d[ri].append(i)
for di in d:
    d[di].append(inf)

#print(d)
right=inf
ans=0
for i in range(n):
    #debug(r[i],right)
    if a[i]%k==0:
        ans+=1
        right=inf
        continue
    next=d[r[i]][bisect_right(d[r[i]],i)]
    if right==i:
        ans+=1  
        right=inf
        continue
    if next<right:
        right=next

print(ans)
"""