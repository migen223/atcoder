import sys

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
ans=0
for i in range(n-1):
    a,b,c=mi()
    a-=1
    b-=1
    graph[a].append((b,c))
    graph[b].append((a,c))
    ans+=2*c

v=[(0,0)]
vis=[-1]*n
vis[0]=0
while v:
    now,dep=v.pop()
    for ne,l in graph[now]:
        if vis[ne]==-1:
            vis[ne]=dep+l
            v.append((ne,dep+l))

ma=max(vis)
v=[]
for i in range(n):
    if vis[i]==ma:
        v.append((i,0))
        break
vis=[-1]*n
vis[v[0][0]]=0
while v:
    now,dep=v.pop()
    for ne,l in graph[now]:
        if vis[ne]==-1:
            vis[ne]=dep+l
            v.append((ne,dep+l))

print(ans-max(vis))
