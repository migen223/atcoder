
n=int(input())

graph=[[] for i in range(n+1)]
for _ in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

v1=[0]*(n+1)
v1[1]=1
vis=[(1,0)]
start=(-1,-1)
while vis:
    now,depth=vis.pop()
    start=max(start,(depth,now))
    #print(now,len(graph[now]))
    for ne in graph[now]:
        if v1[ne]==0:
            v1[ne]=1
            vis.append((ne,depth+1))

vis=[(start[1],0)]
v2=[0]*(n+1)
v2[start[1]]=1
goal=(-1,-1)
while vis:
    now,depth=vis.pop()
    goal=max(goal,(depth,now))
    #print(now,len(graph[now]))
    for ne in graph[now]:
        if v2[ne]==0:
            v2[ne]=1
            vis.append((ne,depth+1))

s=start[1]
g=goal[1]
sdepth=[(-1,-1) for i in range(n+1)]
gdepth=[(-1,-1) for i in range(n+1)]

vis=[(s,0)]
sdepth[s]=(0,s)
while vis:
    now,depth=vis.pop()
    #print(now,len(graph[now]))
    for ne in graph[now]:
        if sdepth[ne][0]==-1:
            sdepth[ne]=(depth+1,s)
            vis.append((ne,depth+1))
    #print(sdepth)

vis=[(g,0)]
gdepth[g]=(0,g)
while vis:
    now,depth=vis.pop()
    #print(now,len(graph[now]))
    for ne in graph[now]:
        if gdepth[ne][0]==-1:
            gdepth[ne]=(depth+1,g)
            vis.append((ne,depth+1))

#print(sdepth)
#print(gdepth)
ans=[]
for i in range(1,n+1):
    ma=max(sdepth[i],gdepth[i])
    ans.append(ma[1])
    print(ma[1])

"""
v2=[0]*(n+1)
dp=[(-1,-1) for i in range(n+1)]

while leaves:
    now=leaves.pop()
    dp[now]=max(dp[now],(depthl[now],now))
    for ne in rgraph[now]:
        v2[ne]+=1
        dp[ne]=max(dp[ne],dp[now])
        if v2[ne]==len(ngraph[ne]):
            leaves.append(ne)

cand=[]
for c in child:
    cand.append(dp[c])
cand.sort()

"""