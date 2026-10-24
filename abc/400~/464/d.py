
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

def solve(l):
    n=len(l)
    dp=[0]*n
    ma=0
    delay=0
    for i in range(n):
        dp[i]=ma+max(l[i],0)
        #debug(ma,delay,l[i])
        
        ma=max(delay,ma)
        delay=dp[i]
        

        
    #print()
    #debug(dp)
    return max(dp)

for _ in range(t):
    n=ii()
    s=input()
    x=li()
    y=li()
    cost=[]
    for i in range(n-1):
        c=0
        if s[i]=="S":
            c+=x[i]
        if s[i+1]=="R":
            c+=x[i+1]
        cost.append(y[i]-c)
    #debug(cost)
    #debug(solve(cost))
    print(solve(cost))

#solve([3,1,1,4,1])
#solve([-2,2,4,3,-9])
