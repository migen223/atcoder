from collections import deque
import sys
n,m=map(int,input().split())
graph=[[] for i in range(n+1)]

for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)

visitable=deque([(1,0)])
visit=[0]*(n+1)
visit[1]=1
while visitable:
    now=visitable.popleft()
    pos=now[0]
    depth=now[1]
    for i in range(len(graph[pos])):
        if graph[pos][i]==1:
            print(depth+1)
            sys.exit()
        else:
            if visit[graph[pos][i]]==0:
                visitable.append((graph[pos][i],depth+1))
                visit[graph[pos][i]]=1

print(-1)
