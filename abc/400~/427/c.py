from itertools import product
n,m=map(int,input().split())
graph=[[] for i in range(n+1)]

for i in range(m):
    v1,v2=map(int,input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

ans=10**9
for p in product([0,1],repeat=n):
    count=0
    for i in range(1,n+1):
        for j in range(len(graph[i])):
            if p[i-1]==p[graph[i][j]-1]:
                count+=1
    ans=min(ans,count//2)
print(ans)
