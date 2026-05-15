from itertools import combinations

n,m=map(int,input().split())
graph=[[] for i in range(n+1)]
for i in range(m):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

ans=0
for c in combinations(range(1,n+1),3):
    if c[0] in graph[c[1]] and c[0] in graph[c[2]]:
        if c[1] in graph[c[0]] and c[1] in graph[c[2]]:
            if c[2] in graph[c[1]] and c[2] in graph[c[0]]:
                ans+=1
print(ans)


