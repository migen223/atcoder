
n,k=map(int,input().split())
a=list(map(int,input().split()))
p=list(map(int,input().split()))
dp=[[0]*n for i in range(k)]
mod=10**9+7

if a[0]==p[0]:
    dp[0][0]=1

for i in range(1,n):
    for j in range(k):
        dp[j][i]=dp[j][i-1]
        if a[i]==p[j]:
            if j==0:
                dp[j][i]+=1
                dp[j][i]%=mod
            else:
                dp[j][i]+=dp[j-1][i-1]
                dp[j][i]%=mod

print(dp[-1][-1]%mod)