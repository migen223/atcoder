from collections import deque
import sys
sys.setrecursionlimit(10**7)

n=int(input())
a=list(map(int,input().split()))
graph=[[] for i in range(n)]
for i in range(n-1):
    u,v=map(lambda x:int(x)-1,input().split())
    graph[u].append(v)
    graph[v].append(u)

ans=["No" for i in range(n)]
def dfs(now,vis,se,flag):
    global ans
    if flag:
        ans[now]="Yes"
    #print(now,vis,se,flag)
    for ne in graph[now]:
        if vis[ne]==0:
            
            vis[ne]=1
            if a[ne] in se:
                ans[ne]="Yes"
                #print(ne,vis,se,flag)
                dfs(ne,vis,se,True)
            else:
                se.add(a[ne])
                #print(ne,vis,se,flag)
                dfs(ne,vis,se,flag)
                se.discard(a[ne])


vis=[0]*n
vis[0]=1
se=set([a[0]])
dfs(0,vis,se,False)
for an in ans:
    print(an)