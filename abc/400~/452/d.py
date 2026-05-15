
s=list(input())
t=list(input())
n=len(s)
m=len(t)
tset=set(t)
dp=[[0 for _ in range(n)] for _ in range(m+1)]
if s[0]==t[0]:
    dp[1][0]+=1
else:
    dp[0][0]+=1

for i in range(1,n):
    if s[i]==t[0]:
        dp[1][i]=dp[0][i-1]+1
        for j in range(1,m):
            if s[i]==t[j]:
                dp[j+1][i]+=dp[j][i-1]
            else:
                dp[j][i]+=dp[j][i-1]
    else:
        dp[0][i]+=dp[0][i-1]+1
        for j in range(1,m):
            if s[i]==t[j]:
                dp[j+1][i]+=dp[j][i-1]
            else:
                dp[j][i]+=dp[j][i-1]

#for i in range(m):
 #   print(*dp[i])

ans=0
for i in range(m):
    for j in range(n):
        ans+=dp[i][j]
print(ans)