import sys
from sortedcontainers import SortedList
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

n=ii()
a=li()
sl=SortedList(a)
sl.add(-inf)
sl.add(inf)
ans=0
now=0
for i in range(n):
    ind=sl.bisect_left(now)
    ne1=sl[ind]
    ne2=sl[ind-1]
    if abs(now-ne1)>=abs(now-ne2):
        ans+=abs(now-ne2)
        now=ne2
        sl.pop(ind-1)
    else:
        ans+=abs(now-ne1)
        now=ne1
        sl.pop(ind)

print(ans)