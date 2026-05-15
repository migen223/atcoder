import heapq
n=int(input())

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
graph=[[] for i in range(n)]
for i in range(n-1):
    a,b,x=map(int,input().split())
    graph[i].append((i+1,a))
    graph[i].append((x-1,b))

ans=dijkstra(graph,0)
print(ans[-1])

