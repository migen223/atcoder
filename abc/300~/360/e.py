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

n,k=mi()

def topro(x,y): #x/y
    return (x*pow(y,-1,mod)%mod)%mod


ans=0
pro1=topro(n*n-2*(n-1),n*n)
pro2=topro(2,n*n)
pros=[pro1,pro2]
for i in range(k-1):
    np1=pros[0]*pro1
    np1+=(n-1)*(pros[1]*pro2)
    np1%=mod
    np2=pros[0]*pro2
    np2+=pros[1]*pro1
    np2+=(n-2)*(pros[1]*pro2)
    np2%=mod
    pros=[np1,np2]

ans=pros[0]
ans+=((n*(n+1))//2-1)*pros[1]
ans%=mod
print(ans)
