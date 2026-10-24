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

n=ii()

def f(a,b):
    return a**3+b*a**2+a*b**2+b**3

def bisearch(a,n):
    l=-1
    r=10**6
    while (r-l)>1:
        #debug(l,r,a)
        m=(l+r)//2
        if f(a,m)>=n:
            r=m
        else:
            l=m
    return r
#debug(bisearch(1,n))

a=0
x=inf
while a**3<=n:
    b=bisearch(a,n)
    x=min(x,f(a,b))
    a+=1
#print(a)
print(x)