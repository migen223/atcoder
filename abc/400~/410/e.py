
n,h,m=map(int,input().split())

dp=[[-1]*(n+1) for _ in range(m+1)]
dp[m][0]=h

for i in range(n):
    a,b=map(int,input().split())
    for j in range(m+1):
        if dp[j][i]>=0:
            dp[j][i+1]=max(dp[j][i+1],dp[j][i]-a)
            if 0<=j-b<=m:
                dp[j-b][i+1]=max(dp[j][i],dp[j-b][i+1])
        
#for i in range(m+1):
 #   print(*dp[i])

ans=0
for i in range(n,-1,-1):
    f=0
    for j in range(m+1):
        if dp[j][i]>=0:
            ans=i
            f+=1
            break
    if f!=0:
        break
print(ans)