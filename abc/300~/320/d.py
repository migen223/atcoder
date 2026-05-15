
n,m=map(int,input().split())
ans=[[] for i in range(n+1)]

graph=[[] for i in range(n+1)]


for i in range(m):
    a,b,x,y=map(int,input().split())
    graph[a].append((b,x,y))
    graph[b].append((a,-x,-y))

ans[1]=[0,0]
visit=[0]*(n+1)
visit[1]=1
visiable=[1]
while visiable:
    now=visiable.pop()
    x=ans[now][0]
    y=ans[now][1]
    for ne,dx,dy in graph[now]:
        if visit[ne]==0:
            visit[ne]=1
            ans[ne]=[x+dx,y+dy]
            visiable.append(ne)

for i in range(1,n+1):
    if len(ans[i])==0:
        print("undecidable")
    else:
        print(*ans[i])
