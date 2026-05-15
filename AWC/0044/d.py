import heapq
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

graph=[[] for  i in range(n+1)]
edge=[]
for i in range(m):
    u,v,w=map(int,input().split())
    edge.append([u,v,w])

if k>0:
    c=list(map(lambda x:int(x)-1,input().split()))
    for ci in c:
        edge[ci][2]*=2

for i in range(m):
    u,v,w=edge[i]
    graph[u].append((v,w))
    graph[v].append((u,w))
#print(graph)

v=[1]
vis=[0]*(n+1)
while v:
    now=v.pop()
    for ne,w in graph[now]:
        if vis[ne]==0:
            vis[ne]+=1
            v.append(ne)

if vis[-1]==0:
    print(-1)
else:
    ans=dijkstra(graph,1)
    print(ans[-1])