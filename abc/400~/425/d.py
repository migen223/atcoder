from collections import deque
h,w=map(int,input().split())
grid=[list(input()) for i in range(h)]

dy=[1,0,-1,0]
dx=[0,1,0,-1]

visitable=deque([])
for i in range(h):
    for j in range(w):
        if grid[i][j]=="#":
            visitable.append([i,j,0])

def check(y,x):
    ans=0
    for i in range(4):
        ny=y+dy[i]
        nx=x+dx[i]
        #print(ny,nx,grid[ny][nx])
        if 0<=nx<=w-1 and 0<=ny<=h-1:
            if grid[ny][nx]=="#":
                ans+=1
        if ans>=2:
            break
    #print(f"ans={ans}")
    if ans==1:
        return True
    else:
        return False

depth=0
stock=[]
ans=len(visitable)

while visitable:
    now=visitable.popleft()
    #print(now)
    y=now[0]
    x=now[1]
    nd=now[2]
    if depth!=nd:
        ans+=len(stock)
        while stock:
            nb=stock.pop()
            grid[nb[0]][nb[1]]="#"
        depth=nd
    
    for i in range(4):
        ny=y+dy[i]
        nx=x+dx[i]
        if 0<=ny<=h-1 and 0<=nx<=w-1:
            if check(ny,nx) and grid[ny][nx]==".":
                visitable.append([ny,nx,nd+1])
                stock.append((ny,nx))
    #print(visitable)

print(ans)