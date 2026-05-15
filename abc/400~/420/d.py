import sys
from collections import deque
h,w=map(int,input().split())
grid=[list(input()) for i in range(h)]

switch=0
dy=[-1,1,0,0]
dx=[0,0,-1,1]

for i in range(h):
    for j in range(w):
        if grid[i][j]=="S":
            s=(i,j,0)

visit=set([(s[0],s[1],0)])
visitable=deque([(s[0],s[1],0,0)])

while visitable:
    now=visitable.popleft()
    y=now[0]
    x=now[1]
    sw=now[2]
    depth=now[3]
    #print(y,x,depth)
    for i in range(4):
        ny=y+dy[i]
        nx=x+dx[i]
        if 0<=ny<h and 0<=nx<w:
            g=grid[ny][nx]
            if (ny,nx,sw) not in visit:
                if g=="S" or g=="." or (sw==0 and g=="o") or (sw==1 and g=="x"):
                    visit.add((ny,nx,sw))
                    visitable.append((ny,nx,sw,depth+1))
                elif g=="G":
                    print(depth+1)
                    sys.exit()
                elif g=="?":
                    visit.add((ny,nx,sw))
                    #visit.add((ny,nx,(sw+1)%2))
                    visitable.append((ny,nx,(sw+1)%2,depth+1))

print(-1)

