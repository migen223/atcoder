
n,k,d=map(int,input().split())
a=list(map(int,input().split()))

dp=[[[-1]*n for _ in range(k)] for _ in range(d)]
dp[a[0]%d][0][0]=a[0]

for i in range(n-1):
    for j in range(k):
        for l in range(d):
            if dp[l][j][i]!=-1:
                ne=dp[l][j][i]+a[i+1]
                dp[l][j][i+1]=max(dp[l][j][i+1],dp[l][j][i])
                dp[a[i+1]%d][0][i+1]=max(dp[a[i+1]%d][0][i+1],a[i+1])
                if j!=k-1:
                    dp[ne%d][j+1][i+1]=max(dp[ne%d][j+1][i+1],ne)

"""
for i in range(d):
    for j in range(k):
        print(*dp[i][j])"""
print(dp[0][-1][-1])