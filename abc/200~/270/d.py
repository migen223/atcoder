import sys

from functools import lru_cache
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
#print(sys.getrecursionlimit())

@lru_cache(maxsize=None)
def dp(n):
    res=0
    #debug(n)
    for i in range(k):
        if n-a[i]>0:
            res=max(n-dp(n-a[i]),res)
        elif n==a[i]:
            res=max(res,n)
    #debug(n,res)
    return res


print(dp(n))