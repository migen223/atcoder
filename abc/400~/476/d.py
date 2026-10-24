import sys

from bisect import bisect_right
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

n,m,k=mi()
x,y=mi()
a=li()
b=li()
b.sort()
a.sort()


ans=0
r=[0]
for i in range(n):
    r.append(r[-1]+a[i])
r.append(inf)

def count(N):
    if N%k==0:
        return N//k
    return N//k+1

def change(N):
    return (k-N%k)%k

#for i in range(m):
 #   print(count(b[i]))

money=x+k*y
ans=bisect_right(r,money)-1
for i in range(m):
    #debug(count(b[i]),y,"Y")
    if count(b[i])>y:
        break
    y-=count(b[i])
    x+=change(b[i])
    res=i+1
    money=x+k*y
    res+=bisect_right(r,money)-1
    ans=max(ans,res)
    #debug(x,y,res)

print(ans)