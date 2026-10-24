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


s=input()
n=len(s)
dic={}

ans=0
for i in range(n):
    ans+=1
    f=0
    for j in range(1,n//2+1):
        if 0<=i-j<n and 0<=i+j<n:
            if s[i-j]==s[i+j]:
                ans+=1
            else:
                if f==1:
                    break
                else:
                    ans+=1
                    f+=1

for i in range(n-1):
    ans+=1
    f=0
    if s[i]!=s[i+1]:
        f=1
    for j in range(1,n//2+1):
        if 0<=i-j<n and 0<=i+j+1<n:
            if s[i-j]==s[i+j+1]:
                ans+=1
            else:
                if f==1:
                    break
                else:
                    ans+=1
                    f+=1

print(ans)