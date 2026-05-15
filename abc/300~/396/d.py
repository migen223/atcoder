from copy import deepcopy
n,m=map(int,input().split())
rabel={}

graph=[[] for i in range(n+1)]
for i in range(m):
    u,v,w=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
    rabel[(u,v)]=w
    rabel[(v,u)]=w
ans=2**64

visitable=[[1,set([1]),-1]]
while visitable:
    now=visitable.pop()
    #print(now)
    pos=now[0]
    vis=now[1]
    xor=now[2]
    if pos==n:
        ans=min(xor,ans)
        continue
    for i in range(len(graph[pos])):
        if graph[pos][i] not in vis:
            nvis=deepcopy(vis)
            nvis.add(graph[pos][i])
            if xor==-1:
                visitable.append([graph[pos][i],nvis,rabel[(graph[pos][i],pos)]])
            else:
                visitable.append([graph[pos][i],nvis,rabel[(graph[pos][i],pos)]^xor])
    #print(visitable)

print(ans)