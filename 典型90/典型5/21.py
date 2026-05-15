import sys
sys.setrecursionlimit(10**7)
n,m=map(int,input().split())
graph=[[] for i in range(n+1)]
rgraph=[[] for i in range(n+1)]

for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    rgraph[b].append(a)



count=1
vl=[-1]*(n+1)
def dfs(now):
    global count,vl
    vl[now]=-2
    for ne in graph[now]:
        if vl[ne]==-1:
            dfs(ne)
    vl[now]=count
    count+=1

for i in range(1,n+1):
    if vl[i]==-1:
        dfs(i)

l=[]
for i in range(1,n+1):
    l.append((vl[i],i))
l.sort(reverse=True)

comp=[]
vis=[-1]*(n+1)

for i in range(n):
    s=l[i][1]
    if vis[s]==-1:
        v=[s]
        res=[s]
        vis[s]=0
        while v:
            now=v.pop()
            for ne in rgraph[now]:
                if vis[ne]==-1:
                    vis[ne]=0
                    res.append(ne)
                    v.append(ne)
        comp.append(res)
#print(comp)
ans=0
for i in range(len(comp)):
    ans+=(len(comp[i])*(len(comp[i])-1))//2
print(ans)
