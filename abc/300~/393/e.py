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

n,k=mi()

a=li()
ma=max(a)
l1=[0]*(ma+ 1)
l2=[0]*(ma+ 1)
l3=[0]*(ma+ 1)
for i in range(n):
    l1[a[i]]+=1

for i in range(1,ma+1):
    for j in range(i,ma+1,i):
        l2[i]+=l1[j]

for i in range(1,ma+1):
    if l2[i]>=k:
        for j in range(i,ma+1,i):
            l3[j]=max(l3[j],i)

for  i in range(n):
    print(l3[a[i]])