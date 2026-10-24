import sys

from bisect import bisect_left,bisect_right
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

n,q=mi()
a=li()
cal1=[0]
for i in range(n):
    cal1.append(cal1[-1]+a[i])
cal2=[0]
for i in range(n):
    cal2.append(cal2[-1]+cal1[i+1])
#print(cal2)
block=[1]
for i in range(1,n):
    block.append(block[-1]+i)



for _ in range(q):
    l,r=mi()
    li=bisect_right(block,l)
    ri=bisect_right(block,r)
    ans=0
    if li==ri:
        l-=block[li-1]
        r-=block[li-1]
        print(cal1[r+1]-cal1[l])
    else:
        l-=block[li-1]
        r-=block[ri-1]
        ans+=cal1[li]-cal1[l]
        ans+=cal1[r+1]
        if ri>=2:
            ans+=cal2[ri-1]-cal2[li]
        print(ans)
        #debug(l,r,li,ri-1," ",cal1[li]-cal1[l],cal1[r+1],cal2[ri-1]-cal2[li])
