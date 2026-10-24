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
dy=[-1,1,1,-1]
dx=[-1,1,-1,1]
#dy=[-1,-1,-1,1,1,1,0,0]
#dx=[-1,0,1,-1,0,1,-1,1]

n=ii()
ay,ax=mi()
by,bx=mi()

grid=[list(input()) for _ in range(n)]

if (ax+ay)%2!=(bx+by)%2:
    print(-1)
    sys.exit()

vis=[[[0 for _ in range(4)] for _ in range(n)] for _ in range(n)]

v=deque([(ay-1,ax-1,0)])
for i in range(4):
    vis[ay-1][ax-1][i]=1
while v:
    y,x,dep=v.popleft()
    #print(y,x,dep)
    if (y,x)==(by-1,bx-1):
        print(dep)
        sys.exit()

    for d in range(4):
        for i in range(1,n):
            ny=y+i*dy[d]
            nx=x+i*dx[d]
            #print(ny,nx,dy[d],dx[d])
            if 0<=ny<=n-1 and 0<=nx<=n-1 :
                if grid[ny][nx]!="#":
                    if  not vis[ny][nx][d]:
                        v.append((ny,nx,dep+1))
                        vis[ny][nx][d]=1
                    else:
                        break
                else:
                    break
            else:
                break
        
print(-1)