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

n=ii()
s=list(input())
d=deque(s)
ans=[]
k=0
if s[0]=="o":
    k+=1
d.popleft()
eat=1
while d:
    while d and k>=1:
        k-=1
        eat+=1
        now=d.popleft()
        if now=="o":
            k+=1
    ans.append(eat)
    k+=1
if not ans:
    ans.append(eat)

while len(ans)<n:
    ans.append(n)
print(*ans)
    
    