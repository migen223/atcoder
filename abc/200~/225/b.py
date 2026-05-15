import sys
n=int(input())

graph=[[] for i in range(n+1)]

for i in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


for i in range(1,n+1):
    if len(graph[i])==n-1:
        print("Yes")
        sys.exit()
print("No")
