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
#dy=[-1,-1,-1,1,1,1,0,0]
#dx=[-1,0,1,-1,0,1,-1,1]

n,m,K=mi()
dp=[[0 for _ in range(K+1)] for _ in range(n+1)]
dp[0][0]=1
p=pow(m,-1,mod)

for i in range(1,1+K):
    dp[n][i]=dp[n][i-1]
    for j in range(n):
        if dp[j][i-1]>0:
            for k in range(1,m+1):
                if j+k<=n:
                    dp[(j+k)%(n+1)][i]+=dp[j][i-1]*p
                    dp[(j+k)%(n+1)][i]%=mod
                else:
                    #debug(n+n-(j+k),j,k)
                    dp[n+(n-(j+k))][i]+=dp[j][i-1]*p
                    dp[n+(n-(j+k))][i]%=mod
    
    #debug(i)
    #for i in range(n+1):
    #    print(*dp[i])

print(dp[-1][-1])
"""



nume=dp[-1][-1]
deno=pow(m,K,mod)
#debug(nume,deno,m,K)
print((nume*pow(deno,-1,mod))%mod)
"""