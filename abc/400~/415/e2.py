
h,w=map(int,input().split())
grid=[list(map(int,input().split())) for i in range(h)]
p=list(map(int,input().split()))

dy=[1,0]
dx=[0,1]

b=[[grid[i][j]-p[i+j] for j in range(w)] for i in range(h)]
dp=[[10**18]*w for i in range(h)]
#print(b)
dp[h-1][w-1]=max(0,-b[h-1][w-1])

for i in range(h-1,-1,-1):
    for j in range(w-1,-1,-1):
        if not (i==h-1 and j==w-1):
            cand=[]
            for d in range(2):
                ny=i+dy[d]
                nx=j+dx[d]
                if 0<=ny<=h-1 and 0<=nx<=w-1:
                    cand.append(dp[ny][nx])
            dp[i][j]=max(0,min(cand)-b[i][j])
#print(dp)
print(dp[0][0])
