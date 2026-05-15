
n,m=map(int,input().split())
graph=[[] for i in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)

ans=0
for i in range(1,n+1):
    visitable=[i]
    visit=set([i])
    #print(visitable)
    while visitable :
        now=visitable.pop()
        #print(now)
        for j in range(len(graph[now])):
            if graph[now][j] not in visit:
                visitable.append(graph[now][j])
                visit.add(graph[now][j])
    ans+=len(visit)
print(ans)
