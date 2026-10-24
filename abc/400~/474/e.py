import sys
from heapq import *
from collections import deque
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


t=ii()
for _ in range(t):
    n=ii()
    al=[]
    bl=[]
    ab=[]
    for _ in range(n):
        a,b=mi()
        al.append(a)
        bl.append(b)
        ab.append((a-b,a,b))
    ab.sort()
    mini=min(al)
    ar=[0]
    br=[0]
    for _,a,b in ab:
        ar.append(ar[-1]+a)
        br.append(br[-1]+b)
    #debug(ar,br)

    ans=inf
    for c in range(n+1):
        res=br[-1]-br[-1-c]
        res+=ar[n-c]
        res+=mini*max(0,2*c-n)
        #debug(res,c)
        ans=min(res,ans)
    debug(ans)
    print(ans)

    """
    for i in range(n//2):
        ord.append(ab[i])
        ord.append(ab[-1-i])
    if n%2==1:
        ord.append(ab[n//2])
    c=0
    ans=0
    while """
    
