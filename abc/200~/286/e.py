import sys
from collections import deque
import heapq
#ダイクストラ法
#edgesは[[(node,weight)]]の形で表されるグラフ　
def dijkstra(edges, start):
    global a
    n=len(edges)
    node=[(inf,inf)]*n
    node[start]=(0,-a[start])
    hq=[]
    heapq.heappush(hq,((0,-a[start]),start))
    while hq:
        now=heapq.heappop(hq)
        pos=now[1]
        weight=now[0]
        #debug(weight,node[pos],pos)
        
        if node[pos]<weight:
            continue
        for i in edges[pos]:
            ne=(weight[0]+i[1][0],weight[1]+i[1][1])
            if ne<node[i[0]]:
                heapq.heappush(hq,(ne,i[0]))
                node[i[0]]=ne
    return node 
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

grid=[input() for _ in range(n)]
graph=[[] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if grid[i][j]=="Y":
            graph[i].append((j,(1,-a[j])))
#print(graph)
route=[]
for i in range(n):
    route.append(dijkstra(graph,i))
    #print(route[i])
q=ii()
for _ in range(q):
    u,v=mmi()
    if route[u][v][0]==inf:
        print("Impossible")
    else:
        print(route[u][v][0],-route[u][v][1])
"""
for _ in range(q):
    U,V=mmi()
    vis=[-1]*n
    vis[U]=1
    v=deque([[U,0,a[U]]])
    ans=[inf,inf]
    cand=[]
    dic={}
    f=0
    while v:
        now,dep,val=v.popleft()
        #debug(vis,now,dep,val)
        if now==V:
            f+=1
            print(dep,val)
            break
        for ne in graph[now]:
            if vis[ne]!=1:
                if ne in dic:
                    dic[ne]=max(dic[ne],val+a[ne])
                else:
                    dic[ne]=val+a[ne]
        #print(dic)
        if not v:
            for d in dic:
                v.append([d,dep+1,dic[d]])
                vis[d]=1
            dic={}
        
    if f==0:
        print("Impossible")
"""