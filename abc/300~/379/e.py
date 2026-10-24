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
sn=[int(s[i]) for i in range(n)]

l=[(i+1)*sn[i] for i in range(n)]
#print(l)
r=[l[0]]
for i in range(1,n):
    r.append(r[-1]+l[i])
#print(r)
ans=deque([])

carry=0
for i in range(n):
    now=r[-i-1]+carry
    ans.appendleft(now%10)
    carry=now//10
    #debug(carry,now)

if carry!=0:
    ans.appendleft(carry)

while ans:
    print(ans.popleft(),end="")
print()
