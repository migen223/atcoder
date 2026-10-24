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

m,d=mi()
s=input()
ans=0
l=[0]*m
for i in range(m):
    if s[i]=="G":
        l[i]=1
        for di in range(1,1+d):
            if 0<=i+di<=m-1:
                l[i+di]=1
            if 0<=i-di<=m-1:
                l[i-di]=1
#print(l)
for i in range(m):
    if l[i]==0:
        ans+=1

print(ans)