
n,m,k=map(int,input().split())

dp=[[0]*(k+1) for i in range(n+1)]
dp[0][0]=1
for i in range(n):
    for j in range(k):
        if dp[i][j]!=0:

            for l in range(1,m+1):
                if j+l<=k:
                    dp[i+1][j+l]+=dp[i][j]
print(sum(dp[n])%998244353)

