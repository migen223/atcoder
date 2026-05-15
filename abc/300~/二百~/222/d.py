
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
p=998244353
ans=0

ma=max(max(a)+1,max(b)+1)

dp=[[0]*n for i in range(ma+1)]

for i in range(a[0],b[0]+1):
    dp[i][0]=1

for i in range(n-1):
    if a[i+1]<=b[i+1]:
        r=[dp[0][i]]
        for j in range(1,ma):
            r.append(r[-1]+dp[j][i])
        for j in range(a[i+1],b[i+1]+1):
            dp[j][i+1]=r[j]%p



for i in range(ma+1):
    ans+=dp[i][-1]
    ans%=p
print(ans)

"""
for i in range(ma+1):
    print(*dp[i])
"""