import sys


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

n=ii()

ran=[]
for  _ in range(n):
    l,r=mi()
    ran.append((l,r))

ans=0
for i in range(n-1):
    l1,r1=ran[i]
    for j in range(i+1,n):
        l2,r2=ran[j]
        res=0
        for k in range(l1,r1+1):
            if k>r2:
                res+=r2-l2+1
            elif l2<k<=r2:
                res+=k-l2
        ans+=res/((r1-l1+1)*(r2-l2+1))


print(ans)