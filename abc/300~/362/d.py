import heapq
n,m=map(int,input().split())
a=list(map(int,input().split()))
graph=[[] for i in range(n+1)]

for i in range(m):
    u,v,b=map(int,input().split())
    graph[u].append((v,b+a[v-1]))
    graph[v].append((u,b+a[u-1]))
#print(graph)
def dijkstra(edges, start):
    
    n=len(edges)
    node=[10**18]*n
    node[start]=a[0]
    hq=[]
    heapq.heappush(hq,(a[0],start))
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
ans=dijkstra(graph,1)
#print(ans)
for i in range(2,n+1):
    print(ans[i],end=" ")
print()

"""
2832044198 2824130042 4696218483 2805069468
2832044198 2824130042 4696218483 2805069468 
2832044198 2824130042 4696218483 2805069468 

"""