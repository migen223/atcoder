
n=int(input())
graph=[[] for i in range(n+1)]
rgraph=[[] for i in range(n+1)]
for i in range(n):
    cp=list(map(int,input().split()))
    c=cp[0]
    p=cp[1:]
    for j in range(c):
        graph[i+1].append(p[j])
        rgraph[p[j]].append(i+1)

ans=[]
ansset=set()
need=[0]*(n+1)
visitable=[1]
while visitable:
    now=visitable.pop()
    for ne in graph[now]:
        if need[ne]==0:
            need[ne]=1
            visitable.append(ne)

count=[len(graph[i]) for i in range(n+1)]
for i in range(1,n+1):
    if need[i]==1 and len(graph[i])==0:
        visitable=[i]
        ans.append(i)
        while visitable:
            now=visitable.pop()
            for ne in rgraph[now]:
                if need[ne]==1:
                    if count[ne]==1:
                        visitable.append(ne)
                        ans.append(ne)
                    count[ne]-=1
                        
print(*ans)
