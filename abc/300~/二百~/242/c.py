
n=int(input())
ans=0

p= 998244353

dp=[[0]*n for i in range(9)]

for i in range(9):
    dp[i][0]=1

for i in range(n-1):
    for j in range(9):
        if j==0:
            dp[j][i+1]=(dp[j][i]+dp[j+1][i])%p
        elif j==8:
            dp[j][i+1]=(dp[j][i]+dp[j-1][i])%p
        else:
            dp[j][i+1]=(dp[j][i]+dp[j+1][i]+dp[j-1][i])%p
"""
for i in range(len(dp)):
    print(*dp[i])
    """
ans=0
for i in range(9):
    ans+=dp[i][n-1]%p
print(ans%p)



