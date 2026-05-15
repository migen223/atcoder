
n,m=map(int,input().split())
x=list(map(int,input().split()))

c=[0]*(n+1)
for i in range(m):
    cn,y=map(int,input().split())
    c[cn]+=y

dp=[[-1]*n for i in range(n+1)]

dp[1][0]=x[0]
dp[0][0]=0
if c[1]!=0:
    dp[1][0]+=c[1]

for i in range(1,n):
    for j in range(n):
        if dp[j][i-1]!=-1:
            dp[0][i]=max(dp[0][i],dp[j][i-1])
            dp[j+1][i]=max(dp[j+1][i],dp[j][i-1]+x[i]+c[j+1])

ans=dp[0][-1]
for i in range(n+1):
    ans=max(ans,dp[i][-1])
print(ans)
