
n,m,k=map(int,input().split())
p=998244353

dp=[[0]*n for _ in range(m+1)]
calc=[[[0,0] for _ in range(n)] for _ in range(m+1)]
for i in range(1,1+m):
    dp[i][0]=1

for i in range(n-1):
    for j in range(1,1+m):
        minus=j-k
        plus=j+k
        if 1<=minus<=m:
            calc[minus][i+1][0]+=dp[j][i]
            calc[minus][i+1][0]%=p
        if 1<=plus<=m:
            calc[plus][i+1][1]+=dp[j][i]
            calc[plus][i+1][1]%=p
    sump=0
    summ=0
    for j in range(1,1+m):
        sump+=calc[j][i+1][1]
        sump%=p
        summ+=calc[-1-j][i+1][0]
        summ%=p
        dp[j][i+1]+=sump
        dp[j][i+1]%=p
        dp[-j-1][i+1]+=summ
        dp[-j-1][i+1]%=p
"""
for i in range(m):
    print(*dp[i])
for i in range(m):
    print(*calc[i])
"""
ans=0
for i in range(1,1+m):
    ans+=dp[i][-1]
    ans%=p
print(ans)