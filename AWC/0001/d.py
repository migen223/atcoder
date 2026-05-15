
n,m,k=map(int,input().split())
ans=0
al=[]
bl=[]
for _ in range(n):
    a,b=map(int,input().split())
    al.append(a)
    bl.append(b)

dp=[[0]*(n) for _ in range(m+1)]
for i in range(k):
    if 0<=i<=n-1 and 0<=m-bl[0]<=m:
        dp[m-bl[0]][i]=al[0]
        ans=max(dp[m-bl[0]][i],ans)

for i in range(n-1):
    cost=bl[i+1]
    val=al[i+1]
    if 0<=m-cost<=m:
        for l in range(k):
            if 0<=i+l+1<=n-1:
                dp[m-cost][i+l+1]=max(dp[m-cost][i+1+l],val)
                ans=max(ans,dp[m-cost][i+l+1])
    for j in range(m+1):
        if dp[j][i]!=0:
            for l in range(k):
                if 0<=i+l+1<=n-1:
                    if 0<=j-cost<=m:
                        dp[j-cost][i+1+l]=max(dp[j-cost][i+1+l],dp[j][i]+val)
                        ans=max(dp[j-cost][i+1+l],ans)
    #for i in range(m+1):
     #   print(*dp[i])
    #print()

"""
for i in range(m+1):
    print(*dp[i])
ans=0
for i in range(m+1):
    ans=max(dp[i][-1],ans)
"""
print(ans)
