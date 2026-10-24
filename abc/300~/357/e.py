import sys
from collections import deque
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

n=ii()
graph=[[] for _ in range(n)]
indig=[0]*n
a=li()
for i in range(n):
    if i==a[i]-1:
        continue
    graph[i].append(a[i]-1)
    indig[a[i]-1]+=1
leaf=deque([])
count=[1]*n
vis=[-1]*n
for i in range(n):
    if indig[i]==0:
        leaf.append(i)
        vis[i]=1
while leaf:
    now=leaf.popleft() 
    vis[now]=1
    #print(now)
    if graph[now]:
        ne=graph[now][0]
        indig[ne]-=1
        count[ne]+=count[now]
        if indig[ne]==0:
            leaf.append(ne)
ans=0
for i in range(n):
    if vis[i]==1:
        ans+=count[i]
#print(vis)
#print(count)
for i in range(n):
    if vis[i]==1:
        continue
    v=[i]
    ind=0
    vis[i]=1
    while ind<len(v):
        now=v[ind]
        ne=graph[now][0]
        if ne!=v[0]:
            vis[ne]=1
            v.append(ne)
            ind+=1
        else:
            break
    #print(v)
    s=0
    for vi in v:
        s+=count[vi]
    ans+=len(v)*s
print(ans)
"""
8
3 4 2 5 2 7 3 4

"""