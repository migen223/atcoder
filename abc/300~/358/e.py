import sys

def debug(*x):print('debug:',*x, file=sys.stderr)
sys.setrecursionlimit(300000)
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
mmi= lambda: map(lambda x:int (x)-1, input().split())
li = lambda: list(mi())
inf = 2 ** 61 - 1
mod = 998244353
#mod=10**9+7
dy=[-1,1,0,0]
dx=[0,0,-1,1]

k=ii()
c=li()
fact=[1,1,2]
for i in range(3,k+1):
    fact.append(fact[-1]*i)
    fact[-1]%=mod
nCk=[[0 for _ in range(k+1)] for  _ in range(k+1)]

def C(n,k):
    return (fact[n]*(pow((fact[n-k]*fact[k])%mod,-1,mod)%mod))%mod
for i in range(1,k+1):
    for j in range(1,i):
        nCk[i][j]=C(i,j)

dp=[[0 for _ in range(26)] for _ in range(k+1)]

for i in range(1,min(k,c[0])+1):
    dp[i][0]+=1

    #debug(i,dp[i][0])
"""
for  i in range(k+1):
    print(i,*dp[i])
print()"""
for i in range(25):
    
    for j in range(1,min(k,c[i+1])+1):
        dp[j][i+1]+=1
    for j in range(1,k+1):
        if dp[j][i]>0:
            dp[j][i+1]+=dp[j][i]
            for l in range(1,min(k,c[i+1])+1):
                if j+l<=k:
                    dp[j+l][i+1]+=dp[j][i]*nCk[j+l][l]
                    dp[j+l][i+1]%=mod
                else:
                    break
        else:
            break
#for  i in range(k+1):
#    print(*dp[i])
ans=0
for i in range(1,1+k):
    ans+=dp[i][-1]
    ans%=mod
print(ans)