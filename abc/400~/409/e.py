
n=int(input())

x=list(map(int,input().split()))
graph=[[] for i in range(n+1)]
weight={}
for i in range(n-1):
    u,v,w=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
    weight[(u,v)]=w
    weight[(v,u)]=w


ngraph=[[] for i in range(n+1)]
rgraph=[[] for i in range(n+1)]
vis=[-1]*(n+1)
v=[1]
vis[1]=1
leafs=[]
while v:
    now=v.pop()
    for ne in graph[now]:
        if vis[ne]==-1:
            vis[ne]=1
            ngraph[now].append(ne)
            rgraph[ne].append(now)
            v.append(ne)
#print(ngraph)
#print(rgraph)

for i in range(2,n+1):
    if len(ngraph[i])==0:
        leafs.append(i)
        
count=[len(ngraph[i]) for i in range(n+1)]
#print(count,leafs)
ans=0
while leafs:
    now=leafs.pop()
    if len(rgraph[now])>0:
        ne=rgraph[now][0]
        count[ne]-=1
        ans+=abs(x[now-1])*weight[(now,ne)]
        x[ne-1]+=x[now-1]
        if count[ne]==0:
            leafs.append(ne)
    #print("leafs",leafs)
    #print("count",count)
print(ans)