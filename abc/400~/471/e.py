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

n,k=mi()
a=li()

fact=[1,1,2]
for i in range(3,2*(10**5)+1):
    fact.append((fact[-1]*i)%mod)

rfact=[]
for i in range(2*(10**5)+1):
    rfact.append((pow(fact[i],-1,mod))%mod)


def C(n,k):
    return (fact[n]*rfact[n-k]*rfact[k])%mod

rn=pow(n,-1,mod)
if k>1:
    ans=0
    nk=C(n,k)
    for i in range(n):
        ans+=(a[i]**2)*(((nk*k)%mod)*rn)
        ans%=mod

    r=[a[0]]
    for i in range(n-1):
        r.append((r[-1]+a[i+1])%mod)
    
    two=0
    for i in range(n-1):
        two+=a[i]*(r[-1]-r[i])
    ans+=two*2*C(n-2,k-2)
    #debug(ans,nk,C(n-2,k-2),two)
    print(ans%mod)
else:
    ans=0
    for i in range(n):
        ans+=a[i]*a[i]
    print(ans%mod)