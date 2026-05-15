from collections import deque
import sys
h,w=map(int,input().split())
grid=[list(input()) for i in range(h)]
for i in range(h):
    for j in range(w):
        x,y=j,i
        if grid[i][j]==">":
            while x<=w-2:
                x+=1
                if grid[y][x]=="." or grid[y][x]=="!":
                    grid[y][x]="!"
                else:
                    break
        elif grid[i][j]=="<":
            while 1<=x:
                x-=1
                if grid[y][x]=="." or grid[y][x]=="!":
                    grid[y][x]="!"
                else:
                    break
        elif grid[i][j]=="^":
            while 1<=y:
                y-=1
                if grid[y][x]=="." or grid[y][x]=="!":
                    grid[y][x]="!"
                else:
                    break
        elif grid[i][j]=="v":
            while y<=h-2:
                y+=1
                if grid[y][x]=="." or grid[y][x]=="!":
                    grid[y][x]="!"
                else:
                    break
        elif grid[i][j]=="S":
            start=(i,j)
"""
for i in range(h):
    print(*grid[i])
"""
visit =[[0]*w for i in range(h)]
visit[start[0]][start[1]]=1
visitable=deque([(start[0],start[1],0)])
dy=[-1,1,0,0]
dx=[0,0,-1,1]
while visitable:
    y,x,move=visitable.popleft()
    for dir in range(4):
        ny=y+dy[dir]
        nx=x+dx[dir]
        if 0<=ny<=h-1 and 0<=nx<=w-1:
            if grid[ny][nx]=="." and visit[ny][nx]==0:
                visit[ny][nx]=1
                visitable.append((ny,nx,move+1))
            elif grid[ny][nx]=="G":
                print(move+1)
                sys.exit()

print(-1)