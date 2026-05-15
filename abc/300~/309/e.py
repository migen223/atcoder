
n,m=map(int,input().split())
p=list(map(int,input().split()))
graph=[[] for i in range(n+1)]

for i in range(n-1):
    graph[p[i]].append(i+2)
#print(graph)
ins=[-1]*(n+1)

for i in range(m):
    x,y=map(int,input().split())
    ins[x]=max(ins[x],y)

visitable=[1]
ans=0
while visitable:
    now=visitable.pop()
    nins=ins[now]
    if nins>=0:
        ans+=1
    for ne in graph[now]:
        ins[ne]=max(ins[ne],nins-1)
        visitable.append(ne)
#print(ins)
print(ans)

