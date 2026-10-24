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
s=input()
ans=[-1]*n
l=0
r=n-1
swap=0

for i in range(n):
    if s[-1-i]=="o":
        swap+=1
    if swap%2==1:
        ans[l]=n-i
        l+=1
    else:
        ans[r]=n-i
        r-=1
    

print(*ans)