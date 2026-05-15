
s=input()
mod= 998244353

n=len(s)
dp=[0]*(n)
dp[0]=1
stock=0
for i in range(1,n):
    dp[i]+=dp[i-1]+1
    dp[i]%=mod
    if s[i]==s[i-1]:
        stock=0
    else:
        stock+=1
    dp[i]+=stock
    dp[i]%=mod
    

print(dp[-1])