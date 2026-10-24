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

def topro(x,y): #x/y
    return (x*(pow(y,-1,mod)%mod))%mod


n,p=mi()

if n==1:
    print(1)
    sys.exit()


fact=[1,1,2]
for i in range(3,n+1):
    fact.append((fact[-1]*i)%mod)
pf=[1,(p*pow(100,-1,mod))%mod]
for i in range(n):
    pf.append((pf[-1]*pf[1])%mod)
q=100-p
qf=[1,(q*pow(100,-1,mod))%mod]
for i in range(n):
    qf.append((qf[-1]*qf[1])%mod)

def C(n,k):
    return (fact[n]*pow((fact[k]*fact[n-k])%mod,-1,mod))%mod
deno=pow(100,-1,mod)%mod

#DP解法
dp=[0]*(n+1)
dp[1]=1
for i in range(2,n+1):
    dp[i]=((dp[i-1]+1)*q+(dp[i-2]+1)*p)*deno
    dp[i]%=mod
print(dp[n])

"""
二項係数解法
ans=0
for ch in range(n//2+1):
    nh=n-2*ch
    res=0
    res+=(C(n-ch,ch)*pf[ch]*qf[n-2*ch])%mod
    if n-2*ch-1>=0:
        res+=(C(n-ch-1,ch)*pf[ch+1]*qf[n-2*ch-1])%mod
    ans+=res*(n-ch)
    ans%=mod
print(ans)
"""
