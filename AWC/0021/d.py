import heapq
from collections import deque
#union-find
from collections import defaultdict
import sys
    
#ダイクストラ法
#edgesは[[(node,weight)]]の形で表されるグラフ　
def dijkstra(edges, start):
    
    n=len(edges)
    node=[10**32]*n
    node[start]=0
    hq=[]
    heapq.heappush(hq,(0,start))
    while hq:
        now=heapq.heappop(hq)
        pos=now[1]
        weight=now[0]
        
        if node[pos]<weight:
            continue
        for i in edges[pos]:
            if weight+i[1]<node[i[0]]:
                heapq.heappush(hq,(weight+i[1],i[0]))
                node[i[0]]=weight+i[1]
    return node 

n,m,k=map(int,input().split())


graph=[[] for i in range(n+1)]
for _ in range(m):
    u,v,t=map(int,input().split())
    graph[u].append((v,t))
    graph[v].append((u,t))


p=list(map(int,input().split()))

vis=set([1])
v=[1]
while v:
    now=v.pop()
    for ne,t in graph[now]:
        if ne not in vis:
            v.append(ne)
            vis.add(ne)

for i in range(k):
    if p[i] not in vis:
        print(-1)
        sys.exit()
if 1 not in vis:
    print(-1)
    sys.exit()
if n not in vis:
    print(-1)
    sys.exit()


dist={}
for i in range(k):
    if p[i] not in dist:
        dist[p[i]]=dijkstra(graph,p[i])
    
if 1 not in dist:
    dist[1]=dijkstra(graph,1)
if n not in dist:
    dist[n]=dijkstra(graph,n)

ans=0
ans+=dist[1][p[0]]
for i in range(1,k):
    ans+=dist[p[i-1]][p[i]]
ans+=dist[p[-1]][n]
#print(dist)
print(ans)