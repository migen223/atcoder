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

"""
dic={}
for i in range(n):
    if a[i] not in dic:
        dic[a[i]]=[-1,i]
    else:
        dic[a[i]].append(i)

for d in dic:
    dic[d].append(inf)

r={}
for d in dic:
    r[d]=[[0,0]]
    for di in dic[d]:
        if di==-1:
            continue
        r[d].append([r[d][-1][0]+1+di,r[d][-1][1]-di*(di+1)])
#print(dic)
print(r)
for _ in range(q):
    L,R=mmi()
    ans=0
    dis=R-L+1
    for d in dic:
        ri=bisect_right(dic[d],R)-1
        li=bisect_left(dic[d],L)-1
        #debug(r)
        f=[r[d][ri][0]-r[d][li][0],r[d][ri][1]-r[d][li][1]]
        ans+=d*(f[0]*dis+f[1])
        #debug(f,ri,li)
    debug(ans)
"""

r1=[0]
r2=[0]
r3=[0]
for i in range(n):
    r1.append(r1[-1]+a[i])
    r2.append(r2[-1]+a[i]*(i+1))
    r3.append(r3[-1]+a[i]*(i+1)**2)



for _ in range(q):
    l,r=mi()
    ans=(r1[r]-r1[l-1])*(1-r*l-l+r)
    ans+=(r2[r]-r2[l-1])*(r+l)
    ans-=r3[r]-r3[l-1]
    print(ans)
