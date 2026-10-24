
n=int(input())
a=list(map(int,input().split()))
mod=998244353

dp=[0]*(n+1)
dp[0]=1
s=1
for i in range(1,1+n):
    dp[i]=s*pow(n,-1,mod)
    s+=dp[i]
    s%=mod
ans=0
for i in range(1,1+n):
    ans+=dp[i]*a[i-1]
    ans%=mod
print(ans)