import sys

from bisect import bisect_right
from collections import defaultdict
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
#(i>>j)&1 →j bit目がたっているかどうか
#i|(1<<j) →iのjbit目を立たせる

n,k,p=mi()
a=li()

pre=[]
aft=[]
for i in range(n):
    if i<n//2:
        pre.append(a[i])
    else:
        aft.append(a[i])

pl=defaultdict(list)
al=defaultdict(list)
for i in range(2**len(pre)):
    res=0
    bit=0
    for j in range(len(pre)):
        if (i>>j)&1:
            bit+=1
            res+=pre[j]
    pl[bit].append(res)

for i in range(2**len(aft)):
    res=0
    bit=0
    for j in range(len(aft)):
        if (i>>j)&1:
            bit+=1
            res+=aft[j]
    al[bit].append(res)

for ai in al:
    al[ai].sort()
for pi in pl:
    pl[pi].sort()

ans=0
for p1 in pl:
    for p2 in pl[p1]:
        if k-p1 not in al:
            continue
        ind=bisect_right(al[k-p1],p-p2)
        ans+=ind
print(ans)