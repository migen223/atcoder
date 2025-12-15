from collections import deque
import sys
h,w=map(int,input().split())
grid=[list(input()) for i in range(h)]

warp={}
for i in range(h):
    for j in range(w):
        if grid[i][j]!="." and grid[i][j]!="#":
            if grid[i][j] not in warp:
                warp[grid[i][j]]=[(i,j)]
            else:
                warp[grid[i][j]].append((i,j))

visit=[[10**7]*w for i in range(h)]
visit[0][0]=1
visitable=deque([(0,0,0)])

dy=[-1,1,0,0]
dx=[0,0,-1,1]
count=0
while visitable:
    y,x,depth=visitable.popleft()
    for i in range(4):
        ny=y+dy[i]
        nx=x+dx[i]
        if 0<=ny<=h-1 and 0<=nx<=w-1:
            if grid[ny][nx]!="#":
                if visit[ny][nx]>depth+1:
                    visit[ny][nx]=depth+1
                    visitable.append((ny,nx,depth+1))
    if grid[y][x]!="." and grid[y][x]!="#":
        while warp[grid[y][x]]:
            ny,nx=warp[grid[y][x]].pop()
            count+=1
            if visit[ny][nx]>depth+1:

                visitable.append((ny,nx,depth+1))
                visit[ny][nx]=depth+1
    #print(visitable)


if visit[h-1][w-1]==10**7:
    print(-1)
else:
    print(visit[h-1][w-1])


#print(count)
"""
for i in range(h):
    print(*visit[i])
"""