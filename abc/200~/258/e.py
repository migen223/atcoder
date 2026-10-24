import sys
from bisect import bisect_left
def debug(*x):print('debug:',*x, file=sys.stderr)
sys.setrecursionlimit(300000)
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 61 - 1
mod = 998244353
#mod=10**9+7
dy=[-1,1,0,0]
dx=[0,0,-1,1]
#dy=[-1,-1,-1,1,1,1,0,0]
#dx=[-1,0,1,-1,0,1,-1,1]

n,q,x=mi()
w=li()
dw=[0]*(2*n)
for i in range(n):
    dw[i]=w[i]
    dw[i+n]=w[i]
r=[0]
for i in range(2*n):
    r.append(r[-1]+dw[i])
s=sum(w)
route=[0]
vis=set([0])
v=[0]
count={}
#ind=bisect_left(r,x%s)
#count[0]=ind+(x//s)*n
while v:
    now=v.pop()
    next=(bisect_left(r,x%s+r[now]))
    #debug(next,x%s+r[now],x%s,now)
    if next%n not in vis:
        vis.add(next%n)
        route.append(next%n)
        v.append(next%n)
        count[now]=next-now+(x//s)*n
    else:
        count[now]=next-now+(x//s)*n
        route.append(next%n)
#print(route)
#print(count)
loop=[]
end=route[-1]
branch=[]
f=0
for i in range(len(route)):
    if f==0:
        if end==route[i]:
            f+=1
            loop.append(route[i])
            continue
        branch.append(route[i])
    else:
        loop.append(route[i])
#print(branch,loop)
loop.pop()
for _ in range(q):
    k=ii()
    if k<=len(branch):
        print(count[branch[k-1]])
    else:
        k-=len(branch)
        print(count[loop[(k-1)%len(loop)]])

"""
5 3 14
1 2 4 2 3
1
2 
3


"""