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
#dy=[-1,-1,-1,1,1,1,0,0]
#dx=[-1,0,1,-1,0,1,-1,1]

n,m=mi()
graph=[[] for _ in range(n)]
for _ in range(m):
    u,v=mmi()
    graph[u].append(v)
    graph[v].append(u)

vis=[-1]*n
part=[]
ans=0
for i in range(n):
    if vis[i]!=-1:
        continue
    vis[i]=0
    v=deque([i])
    route=[i]
    e=0
    e12=[1,0]
    while v:
        now=v.popleft()
        for ne in graph[now]:
            e+=1
            if vis[ne]==-1:
                vis[ne]=vis[now]+1
                e12[vis[ne]%2]+=1
                v.append(ne)
                route.append(ne)
            else:
                if vis[ne]%2==vis[now]%2:
                    print(0)
                    sys.exit()
    ans+=e12[0]*e12[1]-e//2
    part.append(len(route))
#print(part)
if part:
    r=part[0]
    for i in range(1,len(part)):
        ans+=r*part[i]
        r+=part[i]
print(ans)

