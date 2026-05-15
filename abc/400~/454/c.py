
n,m=map(int,input().split())

graph=[[] for i in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)

vis=[0]*(n+1)
vis[1]=1
v=[1]
while v:
    now=v.pop()
    for ne in graph[now]:
        if vis[ne]==0:
            vis[ne]=1
            v.append(ne)

#print(vis)
print(sum(vis))
