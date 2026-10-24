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

t=ii()
dic={}
for i in range(65,91):
    dic[chr(i)]=i-65

for _ in range(t):
    n=ii()
    s=input()
    l=[dic[s[i]]  for i in range(n)]
    #print(l)
    dp=[[0 for _ in range((n+1)//2)]for _ in range(2)]
    for i in range(l[0]):
        dp[0][0]+=1
    dp[1][0]+=1
    for i in range((n+1)//2-1):
        dp[0][i+1]+=dp[0][i]*26
        dp[0][i+1]%=mod
        dp[0][i+1]+=l[i+1]
        dp[0][i+1]%=mod
        dp[1][i+1]+=1
    ans=dp[0][-1]
    x=[0]*n
    for i in range((n+1)//2):
        x[i]=l[i]
        x[-1-i]=l[i]
    if x<=l:
        ans+=1
    print(ans%mod)

    