import sys
n,m=map(int,input().split())

graph=[[] for i in range(n+1)]

for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


for i in range(1,n+1):
    if len(graph[i])>2:
        print("No")
        sys.exit()

unvisit=[True]*(n+1)
for i in range(1,n+1):
    if unvisit[i]:
        visitable=[[i,-1]]
        while visitable:
            now=visitable.pop()
            if not (unvisit[now[0]]):
                print("No")
                sys.exit()
            unvisit[now[0]]=False
            for j in range(len(graph[now[0]])):
                if graph[now[0]][j]!=now[1]:
                    visitable.append([graph[now[0]][j],now[0]])
            #print(visitable)

print("Yes")

