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

#01-BFS
#edgesは[[(node,weight)]]の形で表されるグラフ　
def BFS01(edges, start):
    
    n=len(edges)
    node=[10**32]*n
    node[start]=0
    dq=deque([(0,start)])
    while dq:
        now=dq.popleft()
        pos=now[1]
        weight=now[0]
        if node[pos]<weight:
            continue
        for i in edges[pos]:
            if weight+i[1]<node[i[0]]:
                if i[1]==0:
                    dq.appendleft((weight+i[1],i[0]))
                elif i[1]==1:
                    dq.append((weight+i[1],i[0]))
                node[i[0]]=weight+i[1]
    return node 