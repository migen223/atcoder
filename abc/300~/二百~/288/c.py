
n,m=map(int,input().split())
graph=[[] for i in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

rens=0
visit=set()
for i in range(1,n+1):
    nvisit=set()
    if i not in visit:
        visitable=[i]
        while visitable:
            now=visitable.pop()
            visit.add(now)
            nvisit.add(now)
            for j in graph[now]:
                if j not in visit:
                    visitable.append(j)
        rens+=len(nvisit)-1
print(m-rens)

