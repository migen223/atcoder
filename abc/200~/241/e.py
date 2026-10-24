import sys
from collections import deque
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

n,k=mi()
a=li()

all=[]
loopi=deque([])
s=0
vis=[-1]*n
v=[0]
vis[0]=0
while v:
    now=v.pop()
    s+=a[now]
    all.append(now)
    loopi.append(now)
    ne=s%n
    if vis[ne]==-1:
        v.append(ne)
        vis[ne]=0
    else:
        start=ne
#print(all,start)
loop=[]
ans=0
while loopi[0]!=start and k>=1:
    ans+=a[loopi.popleft()]
    k-=1

if k==0:
    print(ans)
    sys.exit()

loopi=list(loopi)
loop=[a[loopi[i]] for i in range(len(loopi))]
ans+=sum(loop)*(k//len(loop))
for i in range(k%len(loop)):
    ans+=loop[i]
print(ans)

"""
5 6
2 1 6 3 1

"""