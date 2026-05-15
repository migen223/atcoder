
n=int(input())

dp=[[-1]*5 for i in range(n+1)]
hop=[(0,-1,-1)]
for i in range(n):
    t,x,a=map(int,input().split())
    hop.append((t,x,a))

dp[0][0]=0

for i in range(1,n+1):
    t,x,a=hop[i]
    dt=t-hop[i-1][0]
    for k in  range(5):
        for l in range(min(5,dt+1)):
            if 0<=k+l<=4:

                dp[i][k+l]=max(dp[i][k+l],dp[i-1][k])
            if 0<=k-l<=4:
                dp[i][k-l]=max(dp[i][k-l],dp[i-1][k])
    if dp[i][x]!=-1:
        dp[i][x]+=a
print(max(dp[-1]))
            
"""
for i in range(n+1):
    print(*dp[i])
"""
