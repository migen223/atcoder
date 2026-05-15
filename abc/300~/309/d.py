from collections import deque
n1,n2,m=map(int,input().split())
graph=[[] for i in range(n1+n2+1)]

for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

d1=0
d2=0

visit=[-1]*(n1+n2+1)
visit[1]=0
visit[n1+n2]=0

visitable=deque([1])
while visitable:
    now=visitable.popleft()
    d1=max(d1,visit[now])
    depth=visit[now]
    for ne in graph[now]:
        if visit[ne]==-1:
            visit[ne]=depth+1
            visitable.append(ne)

visitable=deque([n1+n2])
while visitable:
    now=visitable.popleft()
    d2=max(d2,visit[now])
    depth=visit[now]
    for ne in graph[now]:
        if visit[ne]==-1:
            visit[ne]=depth+1
            visitable.append(ne)
#print(visit)
print(d1+d2+1)

