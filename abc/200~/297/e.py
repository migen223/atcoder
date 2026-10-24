import sys
from heapq import *
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
a=set(li())
a=list(a)
a.sort()
se=set()
hq=[]
for ai in a:
    heappush(hq,ai)
    se.add(ai)

ans=1

for i in range(k):
    #print(hq)
    ans=heappop(hq)
    for ai in a :
        if ans+ai not in se:
            heappush(hq,ans+ai)
            se.add(ans+ai)
    #debug(ans)
print(ans)