import sys
s=input()
n=len(s)
p=998244353
dp=[[0]*n for i in range(n//2+2)]
if s[0]=="(" or s[0]=="?":
    dp[1][0]=1
else:
    print(0)
    sys.exit()
d=[-1,1]

for i in range(n-1):
    if s[i+1]=="?":
        for j in range(n//2+2):
            if dp[j][i]>0:
                for k in range(2):
                    nj=j+d[k]
                    #print(nj,j,i)
                    if 0<=nj<=n//2+1:
                        dp[nj][i+1]+=dp[j][i]
                        dp[nj][i+1]%=p
    elif s[i+1]=="(":
        for j in range(n//2+2):
            if dp[j][i]>0:
                if 0<=j+1<=n//2+1:
                    dp[j+1][i+1]+=dp[j][i]
                    dp[j+1][i+1]%=p
    else:
        for j in range(n//2+2):
            if dp[j][i]>0:
                if 0<=j-1<=n//2+1:
                    dp[j-1][i+1]+=dp[j][i]
                    dp[j-1][i+1]%=p
"""
for i in range(n//2+2):
    print(*dp[i])
"""
print(dp[0][-1])
