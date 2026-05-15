
n,m=map(int,input().split())
a=list(map(int,input().split()))

asort=sorted(a)
ma=0
for i in range(m):
    ma+=asort[-i-1]*(m-i)


dp=[[-10**12]*m for i in range(n)]
dp[0][0]=a[0]

for i in range(1,n):
    for j in range(m):
        if j==0:
            dp[i][j]=max(dp[i-1][j],a[i],dp[i][j])
        else:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-1]+(j+1)*a[i])


print(dp[-1][-1])
"""
for i in range(n):
    print(*dp[i])

    """