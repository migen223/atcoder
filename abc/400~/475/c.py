import sys

from bisect import bisect_left
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

n,s,l=mi()
a=li()

l1=[]
r1=[]
l2=[]
r2=[]

for i in range(n-1):
    if i<s-1:
        l1.append(a[i]*2)
        l2.append(a[i])
    else:
        r1.append(a[i])
        r2.append(a[i]*2)
l1.reverse()
l2.reverse()

if len(l1)==0:
    ans=1
    su=0
    for i in range(len(r1)):
        if su+r1[i]>l:
            break
        else:
            su+=r1[i]
            ans+=1
    print(ans)
    exit()
elif len(r1)==0:
    ans=1
    su=0
    for i in range(len(l2)):
        if su+l2[i]>l:
            break
        else:
            su+=l2[i]
            ans+=1
    print(ans)
    exit()

debug(l1,r1)
debug(l2,r2)

ans=1

res=0
su=0
i=0
while i<len(r1) :
    if su+r1[i]<l:
        su+=r1[i]
        res+=1
        i+=1
    else:
        break
ans=max(res+1,ans)
ls=0
for j in range(len(l1)):
    ls+=l1[j]
    #debug(res,su,i)
    if ls>l:
        #debug(ls,l)
        break
    while su+l1[j]>l and i>0:
        su-=r1[i-1]
        i-=1
        res-=1
    res+=1
    su+=l1[j]
    ans=max(ans,res+1)
    




res=0
su=0
i=0
while i<len(l2) :
    if su+l2[i]<l:
        su+=l2[i]
        res+=1
        i+=1
    else:
        break
ans=max(res+1,ans)
rs=0
for j in range(len(r2)):
    rs+=r2[j]
    if rs>l:
        break
    while su+r2[j]>l and i>0:
        su-=l2[i-1]
        i-=1
        res-=1
    res+=1
    su+=r2[j]
    ans=max(ans,res+1)
print(ans)