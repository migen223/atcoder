from collections import deque
n=int(input())
graph=[[] for i in range(n+1)]

for _ in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

v=deque([[1,0]])
vis=[-1]*(n+1)
#print(v[0][0])
vis[v[0][0]]=0
while v:
    now,d=v.popleft()
    for ne in graph[now]:
        if vis[ne]==-1:
            vis[ne]=d+1
            v.append((ne,d+1))

ma=[-1,-1]
for i in range(1,n+1):
    if ma[1]<vis[i]:
        ma=[i,vis[i]]

v=deque([[ma[0],0]])
vis=[-1]*(n+1)
vis[v[0][0]]=0
while v:
    now,d=v.popleft()
    for ne in graph[now]:
        if vis[ne]==-1:
            vis[ne]=d+1
            v.append((ne,d+1))


print(max(vis)+1)
