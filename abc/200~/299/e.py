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

dist={i:{j:[] for j in range(n)} for i in range(n)}
#dist[開始頂点][深さ]
for i in range(n):
    v=deque([(i,0)])
    vis=set([i])
    dist[i][0].append(i)
    while v:
        now,d=v.popleft()
        for ne in graph[now]:
            if ne not in vis:
                vis.add(ne)
                v.append((ne,d+1))
                dist[i][d+1].append(ne)


k=ii()
ban=set()
need=[]
if k==0:
    print("Yes")
    ans=[1]*n
    for ai in ans:
        print(ai,end="")
    print()
    sys.exit()

for i in range(k):
    p,d=mi()
    if d==n:
        print("No")
        sys.exit()
    p-=1
    for j in range(min(d,n)):
        for di in dist[p][j]:
            ban.add(di)
    se=set()
    for di in dist[p][d]:
        se.add(di)
    need.append(se)

ans=[0]*n
for ni in need:
    if len(ni-ban)>=1:
        for i in ni-ban:
            ans[i]=1
    else:
        print("No")
        sys.exit()

print("Yes")
for ai in ans:
    print(ai,end="")
print()
