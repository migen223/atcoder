
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))

dp=[[-10**12]*n for i in range(3)]
dp[0][0]=a[0]
for i in range(1,n):
    dp[0][i]=dp[0][i-1]+a[i]
    dp[1][i]=max(dp[1][i],dp[0][i-1]+b[i],dp[1][i-1]+b[i])
    dp[2][i]=max(dp[2][i],dp[1][i-1]+c[i],dp[2][i-1]+c[i])

print(dp[-1][-1])