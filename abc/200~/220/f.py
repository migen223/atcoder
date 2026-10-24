import sys
from collections import deque
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
graph=[[] for _ in range(n)]
for _ in range(n-1):
    u,v=mmi()
    graph[u].append(v)
    graph[v].append(u)

rgraph=[[] for _ in range(n)] #0を根とする根つき木を構築
vis=[-1]*n
v=[0]
vis[0]=1
parent=[-1]*n #各頂点の親を登録　0は-1
child=[0]*n #直接の子供の数
while v:
    now=v.pop()
    for ne in graph[now]:
        if vis[ne]==-1:
            parent[ne]=now
            v.append(ne)
            vis[ne]=1
            rgraph[now].append(ne)
            child[now]+=1

leaf=deque([])
des=[1]*n  #頂点ごとの子孫の数
for i in range(n):
    if child[i]==0:
        leaf.append(i)

while leaf:
    now=leaf.popleft()
    if now==0:
        break
    p=parent[now]
    des[p]+=des[now] #自身の部分木の頂点数を親へと伝播させる
    child[p]-=1 
    if child[p]==0:
        leaf.append(p)

v=[(0,0)]
nows=0 #i=0における各頂点までの距離の和
while v:
    now,dep=v.pop()
    nows+=dep
    for ne in rgraph[now]:
        v.append((ne,dep+1))

ans=[0]*n
ans[0]=nows 
v=[(0,nows)]
while v:
    now,s=v.pop()
    for ne in rgraph[now]:
        ans[ne]=s+((n-des[ne])-des[ne]) #差分更新
        v.append((ne,ans[ne]))
              
for i in range(n):
    print(ans[i])

"""
5
1 4
4 3
3 2
3 5
"""
