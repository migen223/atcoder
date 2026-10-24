import sys

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

n,k=mi()

clo=set()
for _ in range(n):
    l,r=mi()
    clo.add((l,r))
clo=list(clo)
c1=sorted(clo)
dic={}
for i in range(len(clo)):
    dic[clo[i]]=i

def check(m):
    res=[c1[-1][0]-m]
    for i in range(1,len(clo)):
        if c1[-1-i][1]<=res[-1]:
            res.append(c1[-1-i][0]-m)
    #print(res)
    return len(res)>=k
#print(check(2))


l=0
r=10**9+1
#print(clo)
debug(clo,l,r)
if len(clo)>=2:
    while (r-l)>1:
        m=(l+r)//2
        if check(m):
            l=m
        else:
            r=m

    if l==0:
        print(-1)
    else:
        print(l)
else:
    print(-1)