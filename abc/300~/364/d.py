import sys
from collections import defaultdict
from bisect import bisect_left,bisect_right
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

n,q=mi()
a=li()
a.sort()
#dic=defaultdict(int)
#for ai in a:
#    dic[a]+=1

def check(b,d,k):
    s=bisect_left(a,b-d)
    e=bisect_right(a,b+d)
    if e-s>=k:
        return True
    return False

for _ in range(q):
    b,k=mi()
    count=0
    l=-1
    r=2*10**8
    while r-l>1:
        m=(r+l)//2
        if check(b,m,k):
            r=m
        else:
            l=m
    print(r)