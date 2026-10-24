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


n,m=mi()
h=li()
graph=[[] for _ in range(n)]

for _ in range(m):
    u,v=mmi()
    if h[u]>=h[v]:
        graph[v].append((u,h[u]-h[v]))
        graph[u].append((v,0))
    else:
        graph[u].append((v,h[v]-h[u]))
        graph[v].append((u,0))

dist=dijkstra(graph,0)

ansl=[0]*n
ansl[0]=h[0]
for i in range(1,n):
    ansl[i]=h[0]-dist[i]

debug(ansl)
ans=0
for i in range(1,n):
    ans=max(ans,ansl[i]-h[i])
print(ans)