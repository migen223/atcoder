import sys
from heapq import *
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

h,w,Y=mi()

grid=[li() for _ in range(h)] 
sink=[deque([]) for _ in range(Y+1)]
vis=[[-1 for _ in range(w)] for _ in range(h)]
for i in range(h):
    if vis[i][0]==-1:
        if grid[i][0]<=Y:
            vis[i][0]=1
            sink[grid[i][0]].append((i,0))
    if vis[i][-1]==-1:
        if grid[i][-1]<=Y:
            vis[i][-1]=1
            sink[grid[i][-1]].append((i,w-1))
for i in range(w):
    if vis[0][i]==-1:
        if grid[0][i]<=Y:
            vis[0][i]=1
            sink[grid[0][i]].append((0,i))
    if vis[-1][i]==-1:
        if grid[-1][i]<=Y:
            vis[-1][i]=1
            sink[grid[-1][i]].append((h-1,i))

s=h*w
for i in range(1,Y+1):
    #print(sink)
    while sink[i]:
        y,x=sink[i].popleft()
        #debug(y,x,i)
        s-=1
        for d in range(4):
            ny=y+dy[d]
            nx=x+dx[d]
            if 0<=ny<=h-1 and 0<=nx<=w-1 and vis[ny][nx]==-1:
                if grid[ny][nx]<=i:
                    sink[i].append((ny,nx))
                elif grid[ny][nx]<=Y:
                    sink[grid[ny][nx]].append((ny,nx))
                vis[ny][nx]=1
    print(s)


"""
hq=[]
vis=[[-1 for _ in range(w)] for _ in range(h)]
for i in range(h):
    if vis[i][0]==-1:
        heappush(hq,(grid[i][0],i,0))
        vis[i][0]=1
    if vis[i][-1]==-1:
        heappush(hq,(grid[i][-1],i,w-1))
        vis[i][-1]=1
for i in range(w):
    if vis[0][i]==-1:
        heappush(hq,(grid[0][i],0,i))
        vis[0][i]=1
    if vis[-1][i]==-1:
        heappush(hq,(grid[-1][i],h-1,i))
        vis[-1][i]=1

ans=[]
sink=h*w
for i in range(1,Y+1):
    #print(hq,i)
    while hq and hq[0][0]<=i:
        #debug(hq[0],i)
        now,y,x=heappop(hq)
        sink-=1
        for d in range(4):
            ny=y+dy[d]
            nx=x+dx[d]
            if 0<=ny<=h-1 and 0<=nx<=w-1 and vis[ny][nx]==-1:
                vis[ny][nx]=1
                heappush(hq,(grid[ny][nx],ny,nx))
    ans.append(sink)

for i in ans:
    print(i)

"""