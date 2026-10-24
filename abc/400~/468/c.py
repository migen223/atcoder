import sys
from itertools import permutations
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


n=ii()
p=tuple(li())
q=tuple(li())

ans=0
for pi in permutations(range(1,n+1)):
    if p<pi<q:
        ans+=1
print(ans)