from collections import deque
import sys
n,m=map(int,input().split())
nxc=[]
for i in range(m):
    x,y,c=input().split()
    nxc.append((int(x),int(y),c))

nxc.sort()
mi=10**12
for x,y,c in nxc:
    if c=="W":
        mi=min(y,mi)
    else:
        if mi<=y:
            print("No")
            sys.exit()
print("Yes")


"""
black=[]
white=[]
point=set([1,n])
for i in range(m):
    x,y,c=input().split()
    x=int(x)
    y=int(y)
    point.add(x)
    point.add(y)
    if c=="B":
        black.append((x,y))
    else:
        white.append((x,y))

point=sorted(list(point))
po={}
op={}
for i in range(len(point)):
    po[point[i]]=i
    op[i]=point[i]

grid=[[-1]*len(point) for i in range(len(point))]

visitable=deque([])
for i in range(len(black)):
    visitable.append((po[black[i][0]],po[black[i][1]]))
    grid[po[black[i][0]]][po[black[i][1]]]=1

dy=[-1,0]
dx=[0,-1]

while visitable:
    x,y=visitable.popleft()
    for i in range(2):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<=len(point)-1 and 0<=ny<=len(point)-1:
            if grid[nx][ny]==-1:
                visitable.append((nx,ny))
                grid[nx][ny]=1

for i in range(len(white)):
    if grid[po[white[i][0]]][po[white[i][1]]]==1:
        print("No")
        sys.exit()
print("Yes")

"""