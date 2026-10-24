import sys

from itertools import product
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

n,w=mi()

food=[]
for _ in range(n):
    a,b=mi()
    food.append((a,b))

ans=0
for p in product([0,1],repeat=n):
    t=0
    v=0
    f=0
    for pi in range(n):
        if p[pi]==1:
            t+=food[pi][0]
            v+=food[pi][1]
        if v>w:
            f+=1

            break
    if f==0:
        ans=max(ans,t)

print(ans)
