from collections import deque
h,w=map(int,input().split())

grid=[input() for _ in range(h)]

dy=[-1,-1,-1,1,1,1,0,0]
dx=[-1,0,1,-1,0,1,-1,1]

ngrid=[[0 for _ in range(w)] for _ in range(h)]

v=deque([])
vis=[[10**32 for _ in range(w)] for _ in range(h)]
black=0

for i in range(h):
    for j in range(w):
        if grid[i][j]=="#":
            #v.append((i,j))
            #vis[i][j]=0
            black+=1
        else:
            for d in range(8):
                ny=i+dy[d]
                nx=j+dx[d]
                if (0<=ny<=h-1 and 0<=nx<=w-1) and grid[ny][nx]=="#":
                    v.append((i,j))
                    vis[i][j]=0
                    break
#print(v)
while v:
    y,x=v.popleft()
    for d in range(8):
        ny=y+dy[d]
        nx=x+dx[d]
        if 0<=ny<=h-1 and 0<=nx<=w-1:
            if vis[ny][nx]==10**32:
                vis[ny][nx]=vis[y][x]+1
                v.append((ny,nx))
#print(vis)
if black!=h*w and black!=0:
    for i in range(h):
        for j in range(w):
            if vis[i][j]%2==1:
                print("#",end="")
            else:
                print(".",end="")
        print()
elif black==h*w:
    for i in range(h):
        for j in range(w):
            print(".",end="")
        print()
else:
    for i in range(h):
        for j in range(w):
            print(".",end="")
        print()