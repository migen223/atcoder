import sys

def debug(*x):print('debug:',*x, file=sys.stderr)
sys.setrecursionlimit(300000)
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 61 - 1
mod = 998244353
#mod=10**9+7
dy=[-1,1,0,0]
dx=[0,0,-1,1]
#dy=[-1,-1,-1,1,1,1,0,0]
#dx=[-1,0,1,-1,0,1,-1,1]

n=ii()
ans=0
l=[]
def calc(n):
    ans=0
    k=1

    while True:
        quo=n//k
        m=n%k
        change=m//quo+1
        ans+=quo*change
        ans%=mod
        k+=change
        if quo==1:
            return ans

print((n*n-n*(n+1)//2+n-calc(n))%mod)

