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

n,m,y=map(int,input().split())

graph=[[] for _ in range(n+1)]
for i in range(m):
    u,v,t=map(int,input().split())
    u-=1
    v-=1
    graph[u].append((v,t))
    graph[v].append((u,t))

x=list(map(int,input().split()))

for i in range(n):
    graph[-1].append((i,x[i]+y))
    graph[i].append((n,x[i]))

ans=dijkstra(graph,0)

for i in range(1,n):
    print(ans[i],end=" ")
print()