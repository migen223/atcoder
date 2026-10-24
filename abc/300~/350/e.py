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

n,a,x,y=mi()

@lru_cache(maxsize=None)
def solve(n):
    #debug(n)
    if n==0:
        return 0
    mini=solve(n//a)+x
    dice=y
    for i in range(2,7):
        dice+=solve(n//i)/6
    dice*=6/5
    return min(mini,dice)

print(solve(n))