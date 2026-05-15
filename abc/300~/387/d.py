from collections import deque
import sys
h,w=map(int,input().split())
grid=[list(input()) for i in range(h)]

d=[-1,1]
dy=[-1,1,0,0]
dx=[0,0,1,-1]


for i in range(h):
    for j in range(w):
        if grid[i][j]=="S":
            start=(i,j)

visit=set()
visitable=deque([[start[0],start[1],-1,0]])
visit.add((start[0],start[1],-1))
f=0
while visitable:
    now=visitable.popleft()
    y=now[0]
    x=now[1]
    pre=now[2]
    depth=now[3]
    if grid[y][x]=="G":
        print(depth)
        sys.exit()
    if pre==-1:
        for i in range(4):
            ny=y+dy[i]
            nx=x+dx[i]
            if 0<=ny<=h-1 and 0<=nx<=w-1:
                if grid[ny][nx]!="#":
                    if i<=1:
                        visitable.append((ny,nx,0,1))#縦軸移動
                        visit.add((ny,nx,0))
                    else:
                        visitable.append((ny,nx,1,1))#横軸移動
                        visit.add((ny,nx,1))
    elif pre==0:#直前が縦移動
        for i in range(2):
            ny=y
            nx=x+d[i]
            if 0<=ny<=h-1 and 0<=nx<=w-1:
                if grid[ny][nx]!="#"  and grid[ny][nx]!="S" and (ny,nx,1) not in visit:
                    visitable.append((ny,nx,1,depth+1))
                    visit.add((ny,nx,1))
    elif pre==1:#直前が横移動
        for i in range(2):
            ny=y+d[i]
            nx=x
            if 0<=ny<=h-1 and 0<=nx<=w-1:
                if grid[ny][nx]!="#" and grid[ny][nx]!="S" and (ny,nx,0) not in visit:
                    visitable.append((ny,nx,0,depth+1))
                    visit.add((ny,nx,0))

print(-1)