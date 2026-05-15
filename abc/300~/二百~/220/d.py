
n=int(input())
a=list(map(int,input().split()))
p=998244353
dp=[[0]*10 for i in range(n-1)]
dp[0][(a[0]+a[1])%10]+=1
dp[0][(a[0]*a[1]%10)]+=1

for i in range(n-2):
    for j in range(10):
        if  dp[i][j]>=1:
            dp[i+1][(j+a[i+2])%10]+=dp[i][j]
            dp[i+1][(j+a[i+2])%10]%=p
            dp[i+1][(j*a[i+2])%10]+=dp[i][j]
            dp[i+1][(j*a[i+2])%10]%=p
"""
for i in range(n-2):
    print(*dp[i])
"""
for i in range(10):
    print(dp[n-2][i])
