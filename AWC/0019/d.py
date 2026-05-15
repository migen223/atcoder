
n,m,t=map(int,input().split())

dp=[[-1 for _ in range(n)] for _ in range(m+1)]
q=[]
for i in range(n):
    
    a,b,c=map(int,input().split())
    q.append((a,b,c))

if q[0][1]>=t:
    dp[0][0]=q[0][0]
else:
    dp[0][0]=0
    if 0<=q[0][2]<=m:
        dp[q[0][2]][0]=q[0][0]


for i in range(1,n):
    #print(q[i])
    a,b,c=q[i]
    for j in range(m+1):
        if dp[j][i-1]!=-1:
            if b>=t:
                dp[j][i]=max(dp[j][i],dp[j][i-1]+a)
            else:
                dp[j][i]=max(dp[j][i],dp[j][i-1])
                if 0<=j+c<=m:
                    dp[j+c][i]=max(dp[j+c][i],dp[j][i-1]+a)


ans=0
for i in range(m+1):
    ans=max(ans,dp[i][-1])
print(ans)
