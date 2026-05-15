import sys
sys.setrecursionlimit(2*10**6)
n,m=map(int,input().split())

graph=[[] for i in range(n+1)]
for _ in range(m):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

ans=0
def dfs(pos,visit):
    global ans
    ans+=1
    #print(pos,ans)
    #print(pos,visit)
    if ans>=10**6:
        print(10**6)
        sys.exit()
    for ne in graph[pos]:
        if visit[ne]==0:
            visit[ne]=1
            dfs(ne,visit)
            visit[ne]=0
    
visit=[0]*(n+1)
visit[1]=1
dfs(1,visit)
print(ans)