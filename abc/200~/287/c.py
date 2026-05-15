n,m=map(int,input().split())
graph=[[] for i in range(n+1)]
for i in range(m):
    v1,v2=map(int,input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

visitable=[1]
visit=set()
while visitable:
    now=visitable.pop()
    visit.add(now)
    for i in graph[now]:
        if i not in visit:
            visitable.append(i)


if len(visit)==n:
    one=0
    two=0
    for i in range(1,n+1):
        if len(graph[i])==1:
            one+=1
        elif len(graph[i])==2:
            two+=1
    if one==2 and two==n-2:
        print("Yes")
    else:
        print("No")
else:
    print("No")