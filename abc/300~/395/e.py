from collections import deque
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

n,m,x=map(int,input().split())
graph=[[] for i in range(2*n)]
for _ in range(m):
    v1,v2=map(lambda x:int(x)-1,input().split()) 
    graph[v1].append((v2,1))
    graph[v2+n].append((v1+n,1))
for i in range(n):
    graph[i].append((n+i,x))
    graph[n+i].append((i,x))

dij=dijkstra(graph,0)
print(min(dij[n-1],dij[2*n-1]))


"""
graph1=[[] for i in range(n)]
graph2=[[] for i in range(n)]
for _ in range(m):
    v1,v2=map(lambda x:int(x)-1,input().split()) 
    graph1[v1].append(v2)
    graph2[v2].append(v1)
graph=[graph1,graph2]
    

visit=[[10**18]*n,[10**18]*n]
visit[0][0]=0


visitable=deque([(0,0,0)])
count=[0]*n
while visitable:
    pos,depth,mode=visitable.popleft() 
    count[pos]+=1
    if depth+x<visit[(mode+1)%2][pos]:
        visitable.append((pos,depth+x,(mode+1)%2))
        visit[(mode+1)%2][pos]=depth+x
    for ne in graph[mode][pos]:
        if depth+1<visit[mode][ne]:
            if ne!=n-1:
                visitable.append((ne,depth+1,mode))
            visit[mode][ne]=depth+1
   # print(visitable)
            
#print(count)
print(min(visit[0][n-1],visit[1][n-1]))

"""