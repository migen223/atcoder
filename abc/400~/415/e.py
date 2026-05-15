
h,w=map(int,input().split())
grid=[list(map(int,input().split())) for i in range(h)]
p=list(map(int,input().split()))

dy=[1,0,-1,0]
dx=[0,1,0,-1]
r=[p[0]]
for i in range(1,len(p)):
    r.append(r[-1]+p[i])

rgrid=[[0]*w for _ in range(h)]
dp=[[-10**32]*w for _ in range(h)]

dp[0][0]=grid[0][0]-p[0]
rgrid[0][0]=grid[0][0]

#for i in range(h):
 #   print(*depth[i])

for i in range(h):
    for j in range(w):
        for d in range(2):
            ny=i+dy[d]
            nx=j+dx[d]
            if 0<=ny<=h-1 and 0<=nx<=w-1:
                rgrid[ny][nx]=max(rgrid[i][j]+grid[ny][nx],rgrid[ny][nx])
                #print("grid",grid[ny][nx],rgrid[i][j],i,j,ny,nx)
"""
print("rgrid")
for i in range(h):
   print(*rgrid[i])"""

for i in range(h):
    for j in range(w):
        dp[i][j] = r[i+j]-rgrid[i][j]
"""
print("dp")
for i in range(h):
    print(*dp[i])"""

for i in range(h):
    for j in range(w):
        if i+j==0:
            continue
        pre=[]
        for d in range(2,4):
            ny=i+dy[d]
            nx=j+dx[d]
            if 0<=ny<=h-1 and 0<=nx<=w-1:
                pre.append(dp[ny][nx])
        #print("i,j",i,j,pre,dp[i][j],max(min(pre),dp[i][j]))
        dp[i][j]=max(min(pre),dp[i][j])
        #print(dp[i][j])
"""
print()
for i in range(h):
    print(*dp[i])            
"""
    
print(max(0,dp[-1][-1]))