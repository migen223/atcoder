
n=int(input())

ws=[]
hs=[]
bs=[]
for i in range(n):
    w,h,b=map(int,input().split())
    ws.append(w)
    hs.append(h)
    bs.append(b)

dp=[[0]*(sum(ws)+1) for i in range(n)]

dp[0][0]=hs[0]
dp[0][ws[0]]=bs[0]

for i in range(n-1):
    for j in range(sum(ws)+1):
        if dp[i][j]>=1:
            dp[i+1][j]=max(dp[i+1][j],dp[i][j]+hs[i+1])

            dp[i+1][j+ws[i+1]]=max(dp[i+1][j+ws[i+1]],dp[i][j]+bs[i+1])
#print(dp)

ans=0
for i in range(sum(ws)+1):
    if i>=sum(ws)-i:
        ans=max(ans,dp[n-1][i])
print(ans)
