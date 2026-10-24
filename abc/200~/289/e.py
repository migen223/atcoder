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

t=ii()

for i in range(t):
    n,m=mi()
    c=li()
    graph=[[] for _ in range(n)]
    vis=[[-1 for _ in range(n)] for _ in range(n)] #t,a
    vis[0][n-1]=1
    for _ in range(m):
        u,v=mmi()
        graph[u].append(v)
        graph[v].append(u)
    v=deque([[0,n-1,0]])
    f=0
    while v:
        t,a,dep=v.popleft()
        if t==n-1 and a==0:
            f+=1
            print(dep)
            break
        tl=[]
        al=[]
        for ne in graph[t]:
            tl.append(ne)
        for ne in graph[a]:
            al.append(ne)
        for ti in tl:
            for ai in al:
                if c[ai]!=c[ti] and vis[ti][ai]==-1:
                    v.append([ti,ai,dep+1])
                    vis[ti][ai]=1
    if f==0:
        print(-1)
    