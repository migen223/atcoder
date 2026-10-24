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

from atcoder.lazysegtree import LazySegTree
id_=-1
def mapping(f,a):
    if f==-1:
        return a
    return f

def composition(f,g):
    if f==-1:
        return g
    return f
def op(x,y): return max(x,y)
e=-inf



w,n=mi()
seg=LazySegTree(op,e,mapping,composition,id_,[0]*(w+1))

for _ in range(n):
    l,r=mi()
    h=seg.prod(l,r+1)
    seg.apply(l,r+1,h+1)
    print(h+1)