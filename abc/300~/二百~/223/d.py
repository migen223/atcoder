import sys
import heapq
n,m=map(int,input().split())

ans=[-1]*n
graph=[[] for i in range(n+1)]
rgraph=[[] for i in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    rgraph[b].append(a)

zero=[]
for i in range(1,n+1):
    if len(rgraph[i])==0:
        heapq.heappush(zero,i)

#print(graph)
#print(rgraph)

if len(zero)==0:
    print(-1)
    sys.exit()

outs=[len(rgraph[i]) for i in range(n+1)]

ind=0
while zero:
    now=heapq.heappop(zero)
    outs[now]=0
    ans[ind]=now
    ind+=1
    for ne in graph[now]:
        outs[ne]-=1
        if outs[ne]==0:
            heapq.heappush(zero,ne)
        elif outs[ne]<0:
            print(-1)
            sys.exit()
    if ind!=n and len(zero)==0:
        print(-1)
        sys.exit()

print(*ans)