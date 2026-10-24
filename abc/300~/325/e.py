import heapq
from collections import deque
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

n,a,b,c=map(int,input().split())

graph=[[] for _ in range(2*n)]
for i in range(n):
    d=list(map(int,input().split()))

    for j in  range(n):
        if i==j:
            continue
        dj=d[j]
        graph[i].append((j,dj*a))
        graph[i].append((j+n,dj*b+c))
        graph[i+n].append((j+n,dj*b+c))

dij=dijkstra(graph,0)
print(min(dij[n-1],dij[2*n-1]))