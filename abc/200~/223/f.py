import sys
from atcoder.lazysegtree import LazySegTree

INF = 1 << 63


def op(ele1, ele2):
    return min(ele1, ele2)


def mapping(func, ele):
    return func + ele

def composition(func_upper, func_lower):
    return func_upper + func_lower


e = INF
id_ = 0

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


n,q=mi()
s=input()
bra=[]
for i in range(n):
    if s[i]=="(":
        bra.append(1)
    else:
        bra.append(-1)
r=[bra[0]]
for i in range(n-1):
    r.append(r[-1]+bra[i+1])


seg = LazySegTree(op, e, mapping, composition, id_, r)

def out():
    for i in range(n):
        debug(seg.get(i))
    print()

for _ in range(q):
    que,l,r=mi()
    if que==1:
        if bra[l-1]!=bra[r-1]:
            if bra[l-1]==1:
                seg.apply(l-1,r-1,-2)
            else:
                seg.apply(l-1,r-1,2)
        bra[l-1],bra[r-1]=bra[r-1],bra[l-1]
        #out()
    else:
        if l==1:
            su=seg.get(r-1)
            mini=seg.prod(l-1,r)
        else:
           # debug("efam",r-1,l-2)
            su=seg.get(r-1)-seg.get(l-2)
            mini=seg.prod(l-1,r)-seg.get(l-2)
        
        
        #debug(su,mini)
        #"""
        if su==0 and mini>=0:
            print("Yes")
        else:
            print("No")#"""