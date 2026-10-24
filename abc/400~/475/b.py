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

n=ii()
a=li()
ans=[0,0,0]
for ai in a:
    if ai%1000==0:
        continue
    else:
        ai=1000*(ai//1000+1)-ai
        s=str(ai)
        for i in range(len(s)):
            ans[i]+=int(s[-1-i])
        
print(*ans)
