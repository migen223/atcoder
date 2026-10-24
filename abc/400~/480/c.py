import sys

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

n,k,t=mi()
a=li()
a.sort()
a=deque(a)

def ceil(n,a):
    if n%a==0:
        return n//a
    return n//a+1

ans=0
now=0
while a:
    next=a.popleft()
    if next>t:
        break
    if now<next:
        ans+=ceil(next-now,k)
        now=next+k
    else:
        now=max(now,next+k)
    #debug(now,ans,next)

if now<t:
    ans+=ceil(t-now,k)

print(ans)
