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

h,w=mi()

grid=[input() for  _ in range(h)]
n=ii()
for i in range(h):
    for j in range(w):
        if grid[i][j]=="S":
            s=(i,j)
        if grid[i][j]=="T":
            g=(i,j)

med={}
toind={}
for i in range(n):
    r,c,e=mi()
    r-=1
    c-=1
    med[(r,c)]=e
    toind[(r,c)]=i
if s not in med:
    print("No")
    sys.exit()  
toind[g]=i+1
med[g]=0
graph=[[] for i in range(n+1)]
for my,mx in med:
    v=deque([(my,mx,med[(my,mx)])])
    vis=set([(my,mx)])
    while v:
        y,x,dep=v.popleft()
        if dep==0:
            continue
        for d in range(4):
            ny=y+dy[d]
            nx=x+dx[d]
            if 0<=ny<=h-1 and 0<= nx <=w-1 and grid[ny][nx]!="#" and (ny,nx) not in vis and dep>0:
                vis.add((ny,nx))
                v.append((ny,nx,dep-1))
                if (ny,nx) in med:
                    graph[toind[(my,mx)]].append(toind[ny,nx])
#print(graph)
v=[toind[s]]
vis=set([toind[s]])  
while v:
    now=v.pop()
    for ne in graph[now]:
        if ne not in vis:
            vis.add(ne)
            v.append(ne)
            if ne==toind[g]:
                print("Yes")
                sys.exit()
print("No")

"""
#vis=[[[-1 for _ in range(w)] for _ in range(h)] for _ in range(ma+1)]
vis=[[-1 for _ in range(w)] for _ in range(h)]

if s not in med:
    print("No")
    sys.exit()

vis[s[0]][s[1]]=med[s]
v=[(s[0],s[1],med[s])]
while v:
    y,x,p=v.pop()
    debug(y,x,p)
    if (y,x)==g:
        print("Yes")
        sys.exit()
    for d in range(4):
        ny=y+dy[d]
        nx=x+dx[d]
        if 0<=ny<=h-1 and 0<=nx<=w-1 and grid[ny][nx]!="#" and p!=0 and vis[ny][nx]<p-1:
            
            if (ny,nx) in med and p-1<=med[(ny,nx)]:
                vis[ny][nx]=med[(ny,nx)]
                v.append((ny,nx,med[(ny,nx)]))
                continue
            v.append((ny,nx,p-1))
            vis[ny][nx]=p-1

print("No")"""

"""
4 4 
S...
....
....
...T
16
1 1 16
1 2 16
1 3 16
1 4 16
2 1 16
2 2 16
2 3 16
2 4 16
3 1 16
3 2 16
3 3 16
3 4 16
4 1 16
4 2 16
4 3 16
4 4 16
"""