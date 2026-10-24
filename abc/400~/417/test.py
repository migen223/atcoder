from random import randint
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

n=randint(1,10)
pres=[]
pl=[]
al=[]
ap=[]
bl=[]
for _ in range(n):
    p,a,b=randint(1,12),randint(1,12),randint(1,12)
    pl.append(p)
    al.append(a)
    ap.append(a+p)
    bl.append(b)
    pres.append([p,a,b])
ma=max(ap)
dp=[[0 for _ in range(n)] for _ in range(ma+1)]

p,a,b=pres[-1]
for i in range(ma+1):
    if i<=p:
        dp[i][-1]=i+a
    else:
        dp[i][-1]=max(0,i-b)

#for i in range(ma+1):
#    print(*dp[i])

for i in range(n-2,-1,-1):
    p,a,b=pres[i]
    for j in range(ma+1):
        if j<=p:
            #debug(j+a)
            dp[j][i]=dp[j+a][i+1]
        else:
            dp[j][i]=dp[max(0,j-b)][i+1]

#for i in range(ma):
#    print(*dp[i])

r=[bl[0]]
for i in range(1,n):
    r.append(r[-1]+bl[i])

q=10000
for _ in range(q):
    x=randint(0,1000000)

    if x<ma:
        print(dp[x][0])
        #print(dp[x][0],"ans")
    else:
        ind=bisect_left(r,x-ma)
       
        if ind==n or ind==n-1:
            print(x-r[-1])
            #print(x-r[-1],"ans")
        else:
            #debug(ind)
            x-=r[ind]
            print(dp[x][ind+1])
            #print(dp[x][ind+1],"ans")

