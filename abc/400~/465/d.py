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

def solve(start,y,k,ans):
    l=start*k
    r=(start+1)*k-1
    while l<=y:
        #debug(l,r,start)
        ans+=1
        if l<=y<=r:
            return ans
        l=l*k
        r=(r+1)*k-1
    return inf

for _ in range(t):
    x,y,k=mi()
    ans=inf
    if x==y:
        print(0)
        continue
    res=0
    while x>0:
        ans=min(ans,solve(x,y,k,res))
        #print(res,x)
        res+=1     
        x//=k
        if x==y:
            ans=min(ans,res)

    ans=min(ans,solve(0,y,k,res))
    print(ans)
    #debug(ans)

