from collections import deque
import sys
h,w=map(int,input().split())
grid=[list(input()) for i in range(h)]


f=0
start=[]
for i in range(h):
    for j in range(w):
        if grid[i][j]=="E":
            start.append((i,j))
            f+=1
if f==0:
    for i in range(h):
        print("".join(grid[i]))
    sys.exit()

dy=[-1,1,0,0] 
dx=[0,0,-1,1]
dic={0:"v",1:"^",2:">",3:"<"}
visitable=deque([(start[i][0],start[i][1],-1) for i in range(len(start))])
visit=set(start)
while visitable:
    now=visitable.popleft()
    #print(now)
    y=now[0]
    x=now[1]
    dir=now[2]
    if grid[y][x]==".":
        grid[y][x]=dic[dir]
    for i in range(4):
        ny=y+dy[i]
        nx=x+dx[i]
        if 0<=ny<=h-1 and 0<=nx<=w-1:
            if grid[ny][nx]=="." and (ny,nx) not in visit:
                visitable.append((ny,nx,i))
                visit.add((ny,nx))

for i in range(h):
    print("".join(grid[i]))

