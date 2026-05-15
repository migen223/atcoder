
n=int(input())
graph=[set() for i in range(n+1)]
ans=[]
for i in range(n-1):
    u,v=map(int,input().split())
    graph[u].add(v)
    graph[v].add(u)

ma=0
for i in range(1,n+1):
    ma=max(len(graph[i]),ma)

if ma==n-1:
    print(ma)
else:


    sect=set()

    vis=[-1]*(n+1)
    for i in range(1,n+1):
        if len(graph[i])==1:
            vis[i]=0
            v=[(i,-1)] #現在地,親
            while v:
                now,p=v.pop()
                
                if vis[now]!=2:
                    for ne in graph[now]:
                        if vis[ne]==-1:
                            if len(graph[ne])>=2:
                                vis[ne]=vis[now]+1
                            else:
                                vis[ne]=0
                            v.append((ne,now))
                else:
                    for ne in graph[now]:
                        if ne!=p:
                            sect.add((now,ne))
                            vis[ne]=0
                            v.append((ne,now))
            #print(vis)
            break

    vis=[-1]*(n+1)

    for l,r in sect:
        graph[l].discard(r)
        graph[r].discard(l)


    for l,r in sect:
        if vis[l]==-1:
            v=[l]
            vis[l]=0
            res=1
            while v:
                now=v.pop()
                for ne in graph[now]:
                    if vis[ne]==-1:
                        res+=1
                        vis[ne]=0
                        v.append(ne)
            ans.append(res-1)
        if vis[r]==-1:
            v=[r]
            vis[r]=0
            res=1
            while v:
                now=v.pop()
                for ne in graph[now]:
                    if vis[ne]==-1:
                        res+=1
                        vis[ne]=0
                        v.append(ne)
            ans.append(res-1)
    ans.sort()
    print(*ans)
