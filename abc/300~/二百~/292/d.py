import sys
n,m=map(int,input().split())
graph=[[] for i in range(n+1)]
for i in range(m):
    v1,v2=map(int,input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

gcheck=[False]*(n+1)
for i in range(1,n+1):
    if not gcheck[i]:
        ren=[]
        visitable=[i]
        visit=set()
        while visitable:
            now=visitable.pop()
            visit.add(now)
            ren.append(now)
            for j in range(len(graph[now])):
                if graph[now][j] not in visit:
                    visitable.append(graph[now][j])
            #print(visitable)
        edges=0

        for j in ren:
            edges+=len(graph[j])
        #print(ren,edges)
        if edges//2!=len(ren):
            print("No")
            sys.exit()
        for j in range(len(ren)):
            gcheck[ren[j]]=True

print("Yes")


