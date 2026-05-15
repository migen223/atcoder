
n,m=map(int,input().split())
grid=[input() for i in range(n)]

check=[[0]*m for i in range(n)]

ans=1
check[1][1]=1
stop=[[0]*m for i in range(n)]
dy=[-1,1,0,0]
dx=[0,0,-1,1]
stop[1][1]=1
visitable=[(1,1)]
while visitable:
    y,x=visitable.pop()
    for i in  range(4):
        dy1=dy[i]
        dx1=dx[i]
        ny=y    
        nx=x
        if dx1==0:
            for i in range(n):
                if 0<=ny+dy1<=n-1:
                    if grid[ny+dy1][nx]=="#":
                        if stop[ny][nx]==0:
                            visitable.append((ny,nx))
                            stop[ny][nx]=1
                        break
                    else:
                        
                        if check[ny][nx]==0:
                            ans+=1
                            check[ny][nx]=1
                        ny+=dy1
        else:
            for i in range(m):
                if 0<=nx+dx1<=m-1:
                    if grid[ny][nx+dx1]=="#":
                        if stop[ny][nx]==0:
                            stop[ny][nx]=1
                            visitable.append((ny,nx))
                        break
                    else:
                        
                        if check[ny][nx]==0:
                            ans+=1
                            check[ny][nx]=1
                        nx+=dx1
print(ans)

"""
for i in range(n):
    for j in range(m):
        print(stop[i][j],end="")
    print()
print()
for i in range(n):
    for j in range(m):
        print(check[i][j],end="")
    print()
"""



