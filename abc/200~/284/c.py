n,m=map(int,input().split())

graph=[[] for i in range(n+1)]
ans=0
for i in range(m):
    v1,v2=map(int,input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

visit=set()
for i in range(1,n+1):
    if i not in visit:
        ans+=1
        visitable=[i]
        while visitable:
            now=visitable.pop()
            visit.add(now)
            for j in graph[now]:
                if j  not in visit:
                    visitable.append(j)
print(ans)