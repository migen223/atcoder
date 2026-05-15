
t=int(input())

def check(graph,start,goal,ban):
    if start==goal:
        return True
    n=len(graph)
    vis=[0]*n
    visitable=[start]
    vis[start]=1
    for i in ban:
        vis[i]=1
    while visitable:
        now=visitable.pop()
        for ne in graph[now]:
            if vis[ne]==0:
                vis[ne]=1
                visitable.append(ne)
            if ne==goal :
                return True
        #print("check",visitable)
    return False            

for _ in range(t):
    n,m,x,y=map(int,input().split())
    graph=[[] for i in range(n+1)]
    for i in range(m):
        u,v=map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    ans=[]
    v=[0]*(n+1)
    v[x]=1
    vis=[x]
    while vis:
        now=vis.pop()
        ans.append(now)
        if now==y:
            break
        cand=[]
        for ne in graph[now]:
            if v[ne]==0:
                cand.append(ne)
        cand.sort()
        next=-1
        for i in range(len(cand)):
            #print("cand",cand[i],y,ans)
            if check(graph,cand[i],y,ans):
                next=cand[i]
                break
        vis.append(next)
        #print(next)
        v[next]=1
        #print("main",vis)
    print(*ans)


    