
n=int(input())
t=list(map(int,input().split()))

s=sum(t)
dp=[[0]*(s+1) for i in range(n)]
dp[0][t[0]]=1


for i in range(n-1):
    for j in range(1,s+1):
        if dp[i][j]==1:
            dp[i+1][j]=1
            dp[i+1][j+t[i+1]]=1

ans=10**12
for i in range(1,s+1):
    if dp[n-1][i]==1:
        ans=min(ans,max(i,s-i))
print(ans)

