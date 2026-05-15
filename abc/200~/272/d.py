from collections import deque
n,m=map(int,input().split())

grid=[[-1]*n for i in range(n)]
grid[0][0]=0

square=[0]
i=0
while (i+1)**2<=m:
    square.append((i+1)**2)
    i+=1

bem=[]
for i in range(len(square)):
    for j in range(i,len(square)):
        if square[i]+square[j]==m:
            bem.append((i,j))
            bem.append((-i,j))
            bem.append((i,-j))
            bem.append((-i,-j))
            bem.append((j,i))
            bem.append((-j,i))
            bem.append((j,-i))
            bem.append((-j,-i))

visitable=deque([(0,0,0)])

while visitable:
    y,x,depth=visitable.popleft()
    for dy,dx in bem:
        ny=y+dy
        nx=x+dx
        if 0<=ny<=n-1 and 0<=nx<=n-1:
            if grid[ny][nx]==-1:
                grid[ny][nx]=depth+1
                visitable.append((ny,nx,depth+1))


for i in range(n):
    print(*grid[i])
