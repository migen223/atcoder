import sys
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

n,q=mi()
a=li()
b=li()
graph=[[] for _ in range(n+1)]
for i in range(n):
    graph[i].append(((i+1)%n,a[i]))
    graph[(i+1)%n].append((i,a[i]))

for i in range(n):
    graph[i].append((n,b[i]))
    graph[n].append((i,b[i]))

dist=dijkstra(graph,n)
#print(dist)
r=[0]
for i in range(2*n):
    r.append(r[-1]+a[i%n])
#print(r,rr)
for _ in range(q):
    s,t=mi()
    if t==n+1:
        print(dist[s-1])
    else:
        ans=inf
        ans=min(ans,r[t-1]-r[s-1])
        ans=min(ans,r[s+n-1]-r[t-1])
        ans=min(ans,dist[s-1]+dist[t-1])
        print(ans)

"""
5 3
1 3 4 2 5
5 2 4 3 7
2 4
1 3
1 4
"""