
n=int(input())
s=input()

dic={"t":1,"c":2,"o":3,"d":4,"e":5,"r":6}
dp=[[0 for _ in range(n)] for _ in range(7)]
mod=10**9+7
if s[0]=="a":
    dp[0][0]+=1

for i in range(1,n):
    for j in range(7):
        dp[j][i]=dp[j][i-1]
    sj=s[i]
    if sj in dic:
        dp[dic[sj]][i]+=dp[dic[sj]-1][i-1]
        dp[dic[sj]][i]%=mod
    elif sj=="a":
        dp[0][i]+=1
        dp[0][i]%=mod

print(dp[-1][-1])

