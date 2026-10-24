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

ans=0

a0=1
leng=3

def check(m,leng,a0):
    now=a0
    mult=a0
    for i in range(leng-1):
        now+=m
        mult*=now
        if mult>n:
            return False
    return True


while a0*(a0+1)*(a0+2)<=n:
    l=0
    r=10**9+1
    while (r-l)>1:
        m=(l+r)//2
        if check(m,leng,a0):
            l=m
        else:
            r=m
    if l==0:
        break
    ans+=l
    a0+=1

a0=1
while a0*(a0+1)*(a0+2)*(a0+3)<=n:
    leng=4
    f=0
    while leng<=20:
        l=0
        r=10**9+1
        while (r-l)>1:
            m=(l+r)//2
            if check(m,leng,a0):
                l=m
            else:
                r=m
        if l==0:
            if leng==3:
                f+=1
            break
        ans+=l
        #debug(ans,leng,"a0",a0,"d",l)
        leng+=1
    #debug(a0,ans)
    if f>0:
        break
    a0+=1
print(ans)
