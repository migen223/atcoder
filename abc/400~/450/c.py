
h,w=map(int,input().split())
grid=[input() for i in range(h)]
#print(grid)
start=[]
for i in range(h):
    for j in range(w):
        if grid[i][j]==".":
            start.append((i,j))

vis=[[0 for _ in range(w)] for _ in range(h)]
dy=[-1,1,0,0]
dx=[0,0,-1,1]
ans=0

while start:
    i,j=start.pop()
    if vis[i][j]==1:
        continue
    #print(i,j)
    f=0
    v=[(i,j)]
    while v:
        y,x=v.pop()
        for d in range(4):
            ny=y+dy[d]
            nx=x+dx[d]
            if 0<=ny<=h-1 and 0<=nx<=w-1:
                if vis[ny][nx]==0 and grid[ny][nx]==".":
                    v.append((ny,nx))
                    vis[ny][nx]+=1
            else:
                f+=1
    if f==0:
        ans+=1
        
print(ans)