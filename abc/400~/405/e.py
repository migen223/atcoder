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

a,o,b,g=mi()
fact=[1,1,2]
for i in range(3,3*10**6+1):
    fact.append((fact[-1]*i)%mod)

ans=0

for i in range(b+1):
    l=(fact[a+o+i]*pow(fact[o],-1,mod)*pow(fact[a+i],-1,mod))%mod
    r=(fact[g-1+b-i]*pow(fact[g-1],-1,mod)*pow(fact[b-i],-1,mod))%mod
    ans+=l*r
    ans%=mod
print(ans)
