import sys
from collections import deque
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

n,m=mi()

graph=[[] for _ in range(n)]
for i in range(m):
    a,b=mi()
    a-=1
    b-=1
    graph[a].append(b)
    graph[b].append(a)

q=ii()

for _ in range(q):
    x,k=mi()
    x-=1
    vis=set([x])
    v=deque([(x,0)])
    ans=x+1
    while v:
        now,dep=v.popleft()
        for ne in graph[now]:
            if ne not in vis and dep+1<=k:
                vis.add(ne)
                v.append((ne,dep+1))
                ans+=ne+1
    print(ans)

