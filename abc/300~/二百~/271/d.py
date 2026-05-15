
n,s=map(int,input().split())

cards=[]
al=[]
bl=[]

for i in range(n):
    a,b=map(int,input().split())
    al.append(a)
    bl.append(b)

ma=10**4+1

dp=[[-1]*ma for i in range(n)]

dp[0][al[0]]=(-1,"H")
dp[0][bl[0]]=(-1,"T")

for i in range(1,n):
    for j in range(ma):
        if dp[i-1][j]!=-1:
            dp[i][j+al[i]]=(j,"H")
            dp[i][j+bl[i]]=(j,"T")

if dp[-1][s]==-1:
    print("No")
else:
    ans=[]
    now=s
    for i in range(n):
        ans.append(dp[-1-i][now][1])
        now=dp[-1-i][now][0]
    print("Yes")
    ans.reverse()
    print(("".join(ans)))




"""
for i in range(len(dp)):
    print(*dp[i])
"""


