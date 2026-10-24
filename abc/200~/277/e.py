import sys
from heapq import *
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

n,m,k=mi()
graph=[[] for _ in range(2*n)]
for _ in range(m):
    u,v,a=mi()
    u-=1
    v-=1
    graph[u+n*a].append(v+n*a)
    graph[v+n*a].append(u+n*a)

s=li()
for i in range(k):
    graph[s[i]-1].append(s[i]+n-1)
    graph[s[i]-1+n].append(s[i]-1)

vis=[-1]*(2*n)
vis[n]=1
v=[]
heappush(v,(0,n))
while v:
    dep,now=heappop(v)
    #debug(now,dep)
    if now%n==n-1:
        print(dep)
        sys.exit()
    for ne in graph[now]:
        #debug(ne)
        if vis[ne]==-1:
            nd=dep
            if abs(now-ne)<n:
                nd+=1
            vis[ne]=1
            heappush(v,(nd,ne))
print(-1)