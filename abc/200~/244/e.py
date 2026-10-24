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

n,m,k,s,t,x=mi()
s-=1
t-=1
x-=1
dp=[[[0,0] for _ in range(k+1)] for _ in range(n)]
edge=[]
for _ in range(m):
    u,v=mmi()
    edge.append((u,v))

dp[s][0][0]+=1

for i in range(1,k+1):
    for u,v in edge:
        if u==x:
            for j in range(2):
                dp[u][i][(j+1)%2]+=dp[v][i-1][j]
                dp[v][i][j]+=dp[u][i-1][j]
                dp[u][i][(j+1)%2]%=mod
                dp[v][i][j]%=mod
        elif v==x:
            for j in range(2):
                dp[v][i][(j+1)%2]+=dp[u][i-1][j]
                dp[u][i][j]+=dp[v][i-1][j]
                dp[v][i][(j+1)%2]%=mod
                dp[u][i][j]%=mod

        else:
            for j in range(2):
                dp[u][i][j]+=dp[v][i-1][j]
                dp[v][i][j]+=dp[u][i-1][j]
                dp[u][i][j]%=mod
                dp[v][i][j]%=mod

#for i in range(n):
 #   print(*dp[i])

print(dp[t][-1][0])

