
n,m=map(int,input().split())
ans=[]
graph=[[] for i in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
#print(graph)
for i in range(1,n+1):
    k=n-len(graph[i])-1
    if k>=3:
       
        ans.append((k*(k-1)*(k-2))//6)
    else:
        ans.append(0)
print(*ans)

