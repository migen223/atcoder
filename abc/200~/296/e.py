import sys

from functools import lru_cache
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

n=ii()
a=li()
a=[a[i]-1 for i in range(n)]
vis=[-1]*n
ans=0
for i in range(n):
    if vis[i]==1:
        continue
    vis[i]=1
    v=[i]
    ind=0
    se=set([i])
    f=0
    while True:
        now=v[ind]
        ne=a[now]
        if vis[ne]==-1:
            ind+=1
            v.append(ne)
            vis[ne]=1
            se.add(ne)
        else:
            if ne in se:
                v.append(ne)
                f+=1
                #print(v)
            break
    #print(v)
    if f==1:
        last=v.pop()
        while v[-1]!=last:
            v.pop()
            ans+=1
        ans+=1
print(ans)
            