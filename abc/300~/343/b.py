n=int(input())
graph=[]
for i in range(n):
    graph.append(list(map(int,input().split())))
for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            print(j+1,end=" ")
    print()
