
h,w=map(int,input().split())
grid=[list(input()) for i in range(h)]
dy=[-1,1,0,0]
dx=[0,0,-1,1]

for i in range(h):
    for j in range(w):
        if grid[i][j]=="#":
            for k in range(4):
                ny,nx=i+dy[k],j+dx[k]
                if 0<=ny<=h-1 and 0<=nx<=w-1:
                    if grid[ny][nx]==".":
                        grid[ny][nx]="m"


visit=[[-1]*w for i in range(h)]
ans=1
for i in range(h):
    for j in range(w):
        
        if visit[i][j]==-1 and grid[i][j]==".":
            visit[i][j]=1
            visitable=[(i,j)]
            free=1
            se=set()
            while visitable:
                y,x=visitable.pop()
                for k in range(4):
                    ny,nx=y+dy[k],x+dx[k]
                    if 0<=ny<=h-1 and 0<=nx<=w-1:
                        if grid[ny][nx]=="." and visit[ny][nx]==-1:
                            visit[ny][nx]=1
                            visitable.append((ny,nx))
                            free+=1
                        elif grid[ny][nx]=="m" :
                            se.add((ny,nx))
            #print(i,j,free)
            free+=len(se)
            ans=max(ans,free)

print(ans)