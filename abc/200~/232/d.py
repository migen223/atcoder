from collections import deque
h,w=map(int,input().split())
grid=[list(input()) for i in range(h)]

ans=1

dy=[0,1]
dx=[1,0]

dp=[[-1]*w for i in range(h)]
dp[0][0]=1
for i in range(h):
    for j in range(w):
        ans=max(ans,dp[i][j])
        if dp[i][j]!=-1:
            for k in range(2):
                ny=i+dy[k]
                nx=j+dx[k]
                if 0<=ny<h and 0<=nx<w:
                    if grid[ny][nx]=="#":
                        continue
                    else:
                    
                        dp[ny][nx]=max(dp[i][j]+1,dp[ny][nx])

#for i in range(h):
 #   print(*dp[i])

print(ans)
"""

visitable=deque([[0,0,1]])

while visitable:
    now=visitable.popleft()
    x=now[0]
    y=now[1]
    d=now[2]
    ans=max(ans,d)
    grid_max[y][x]=d
    for i in range(2):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<w and 0<=ny<h:
            if grid[ny][nx]!="#":
                if grid_max[ny][nx]<d+1:
                    visitable.append([nx,ny,d+1])

print(ans)
"""