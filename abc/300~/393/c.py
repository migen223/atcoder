n,m=map(int,input().split())
graph=[set() for i in range(n)]
ans=0
for i in range(m):
    v1,v2=map(int,input().split())
    if v1==v2:
        ans+=1
        #print(f"v1=v2 {ans}")
        continue
    if v2-1 in graph[v1-1]:
        ans+=1
        #print(f"多重辺 {ans}")
    graph[v1-1].add(v2-1)
    graph[v2-1].add(v1-1)
    #print(graph)
    
print(ans)