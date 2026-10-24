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
#インタラクティブ問題で使用するときは必ずprintにflush=Trueをつける

n=ii()

def C(l):
    n=l[1]-l[0]+1
    return n*(n-1)//2

r=2
res=[]
f=0
for i in range(1,n):
    l=i
    if l==r:
        r+=1
    f=0
    while r<=n:
        print("?",l,r,flush=True)
        a=input()
        if a=="Yes":
            r+=1
        else:
            if r-l>=2:
                res.append((l,r-1))
                f+=1
            break
    if f==0:
        res.append((l,r-1))
#print(res)
ans=0
for ri in res:
    ans+=ri[1]-ri[0]
print("!",ans,flush=True)
sys.exit()