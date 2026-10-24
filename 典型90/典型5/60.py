import sys

from bisect import bisect_left
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

l=[a[0]]
r=[a[-1]]
lc=[0]*n
lc[0]=1
rc=[0]*n
rc[0]=1

for i in range(1,n):
    ind=bisect_left(l,a[i])  
    if ind==len(l):
        l.append(a[i])
    else:
        l[ind]=a[i]
    lc[i]=len(l)

for i in range(1,n):
    ind=bisect_left(r,a[-1-i])  
    if ind==len(r):
        r.append(a[-1-i])
    else:
        r[ind]=a[-1-i]
    rc[i]=len(r)

#print(lc,rc)
ans=0
for i in range(n):
    ans=max(ans,lc[i]+rc[-1-i]-1)
print(ans)