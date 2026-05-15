
n,m=map(int,input().split())
graph=[[] for i in range(n+1)]
graph2=[[] for i in range(n+1)]
for i in range(m):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph2[y].append(x)

color=[0]*(n+1)

q=int(input())
for i in range(q):
    que,v=map(int,input().split())
    if que==1:
        if color[v]==0:
            visitable=[v]
            color[v]=1
            while visitable:
                now=visitable.pop()
                for j in graph2[now]:
                    if color[j]==0:
                        color[j]=1
                        visitable.append(j)
    else:
        if color[v]==1:
            print("Yes")
        else:
            print("No")
                



