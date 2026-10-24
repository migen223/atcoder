import sys

def debug(*x):print('debug:',*x, file=sys.stderr)
sys.setrecursionlimit(300000)
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 61 - 1
mod = 998244353
#mod=10**9+7
dy=[-1,1,0,0]
dx=[0,0,-1,1]
#dy=[-1,-1,-1,1,1,1,0,0]
#dx=[-1,0,1,-1,0,1,-1,1]

n,q=mi()
graph=[[] for _ in range(n+1)]
for _ in range(q):
    l,r=mi()
    graph[l-1].append(r)
    graph[r].append(l-1)

vis=[-1]*(n+1)
vis[0]=0
v=[0]
while v:
    now=v.pop()
    if now==n:
        print("Yes")
        sys.exit()
    for ne in graph[now]:
        if vis[ne]==-1:
            v.append(ne)
            vis[ne]=0
print("No")