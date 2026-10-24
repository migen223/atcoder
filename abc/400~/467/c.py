import sys
from collections import deque
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

n,m=mi()
a=li()
b=li()

"""
l=[]
for i in range(n-1):
    if (a[i]+a[i+1])%m==b[i]:
        l.append(1)
    else:
        l.append(0)
print(l)
ans=0
for i in range(n-1):
    if l[i]%2==0:
        l[i]+=1
        if 0<=i+1<len(l):
            l[i+1]+=1
        ans+=1
print(ans)"""


if (a[0]+a[1])%m==b[0]:

    ans=0
    a1=[a[i] for i in range(n)]
    for i in range(n-1):
        if (a[i]+a[i+1])%m==b[i]:
            continue
        a[i+1]+=1
        ans+=1
    ans1=2
    a1[0]+=1
    a1[1]+=1 
    for i in range(1,n-1):
        if (a1[i]+a1[i+1])%m==b[i]:
            continue
        a1[i+1]+=1
        ans1+=1
    print(min(ans1,ans))

else:
    ans1=0
    ans2=0
    a1=[a[i] for i in range(n)]
    a2=[a[i] for i in range(n)]
    a1[0]+=1
    ans1+=1
    for i in range(1,n-1):
        if (a1[i]+a1[i+1])%m==b[i]:
            continue
        a1[i+1]+=1
        ans1+=1
    a2[1]+=1
    ans2+=1
    for i in range(1,n-1):
        if (a2[i]+a2[i+1])%m==b[i]:
            continue
        a2[i+1]+=1
        ans2+=1
    print(min(ans1,ans2))

"""
l=deque([])
for i in range(n-1):
    if (a[i]+a[i+1])%2!=b[i]:
        l.append(i)
if not l:
    print(0)
    sys.exit()

ren=[[l[0]]]
for i in range(1,len(l)):
    if ren[0][-1]+1==l[i]:
        ren[-1].append(l[i])
    else:
        ren.append([l[i]])

def ceil(n):
    if n%2==0:
        return n//2
    else:
        return n//2+1

for  i in range(len(ren)):
    ans+=ceil(len(ren[i]))
print(ans)"""