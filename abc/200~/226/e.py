import sys
from itertools import product
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

n,m=mi()
e=[]
graph=[[] for _ in range(n)]
for _ in range(m):
    u,v=mmi()
    e.append((u,v))
    graph[u].append(v)
    graph[v].append(u)

vis=[-1]*n
for i in range(n):
    if vis[i]==1:
        continue
    v=[(i,-1)]
    en=0
    tn=1
    f=0
    while v:
        now,par=v.pop()
        for ne in graph[now]:
            if vis[ne]==-1:
                tn+=1
                en+=1
                vis[ne]=1
                v.append((ne,now))
            else:
                if ne!=par:
                    f+=1
    #debug(en,tn)
    if f==0:
        print(0)
        sys.exit()
                

vis=[-1]*n
leaf=[]
count=[len(graph[i]) for i in range(n)]
for i in range(n):
    if len(graph[i])==1:
        leaf.append(i)

while leaf:
    now=leaf.pop()
    vis[now]=1
    for ne in graph[now]:
        if vis[ne]==-1:
            count[ne]-=1
            if count[ne]==1:
                leaf.append(ne)
ans=1
f=0
for i in range(n):
    if vis[i]!=-1:
        continue
    en=0 #今回のループにおける辺の数
    tn=1    #今回のループにおける頂点の数
    nowl=[i] #頂点たち
    v=[i]
    vis[i]=0
    #debug(ans,i)
    while v:
        now=v.pop()
        for ne in graph[now]:
            if vis[ne]==-1:
                tn+=1
                vis[ne]=0
                v.append(ne)
                nowl.append(ne)
            if vis[ne]==-1 or vis[ne]==0:
                en+=1
    #print(en)
    if en//2==tn:
        f+=1
        ans*=2
        ans%=mod
    else:
        print(0)
        sys.exit()
    for li in nowl:
        vis[li]=1
    #print(vis)
if f==0:
    ans=0
print(ans)
    #debug(ans)

"""
ans1=0
for p in product([0,1],repeat=m):
    graph=[[] for _ in range(n)]
    for i in range(m):
        u,v=e[i]
        if p[i]==0:
            graph[u].append(v)
        else:
            graph[v].append(u)
    f=0
    for i in range(n):
        if len(graph[i])!=1:
            f+=1
            break
    if f==0:
        ans1+=1
print(ans==ans1,ans,ans1)"""