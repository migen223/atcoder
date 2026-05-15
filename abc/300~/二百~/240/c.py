import sys
n,x=map(int,input().split())
dp=[[0]*(x+1) for i in range(n+1)]
dp[0][0]=1
a=[]
b=[]
for i in range(n):
    an,bn=map(int,input().split())
    a.append(an)
    b.append(bn)

for i in range(n):
    for j in range(x+1):
        if dp[i][j]==1:
            if j+a[i]<=x:
                dp[i+1][j+a[i]]=1
            if j+b[i]<=x:
                dp[i+1][j+b[i]]=1



#print(*dp)
if dp[n][x]==1:
    print("Yes")
else:
    print("No")

