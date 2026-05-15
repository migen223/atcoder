h,w=map(int,input().split())
grid=[list(input()) for i in range(h)]

dy=[1,1,1,-1,-1,-1,0,0]
dx=[0,1,-1,0,1,-1,1,-1]
visit=set()
ans=0
for i in range(h):
    for j in range(w):
        if grid[i][j]=="#" and (i,j) not in visit:
            visitable=[[i,j]]
            while visitable:
                now=visitable.pop()
                visit.add((now[0],now[1]))
                for k in range(8):
                    ny=now[0]+dy[k]
                    nx=now[1]+dx[k]
                    if 0<=ny<=h-1 and 0<=nx<=w-1:
                        if grid[ny][nx]=="#" and (ny,nx) not in visit:
                            visitable.append([ny,nx])
            ans+=1
print(ans)

            
            
