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

h,w,k=mi()

grid=[list(input()) for _ in range(h)]
banrow=set()
banline=set()
for  i in range(h):
    for j in range(w):
        if grid[i][j]=="#":
            banrow.add(j)
            banline.add(i)
    
safe=deque([])
vis=[[-1 for _ in range(w)] for _ in range(h)]
for i in range(h):
    for j in range(w):
        if i not in banline and j not in banrow:
            safe.append((i,j,0))
            vis[i][j]=0

#debug(safe)
while safe:
    y,x,dep=safe.popleft()
    for d in range(4):
        ny=y+dy[d]
        nx=x+dx[d]
        if 0<=ny<=h-1 and 0<=nx<=w-1 and vis[ny][nx]==-1 and grid[ny][nx]!="#":
            vis[ny][nx]=dep+1
            safe.append((ny,nx,dep+1))

ans=0
for i in range(h):
    for j in range(w):

        if vis[i][j]<=k and vis[i][j]!=-1:
            ans+=1

#debug(ans)
##   print(*vis[i])

print(ans)
