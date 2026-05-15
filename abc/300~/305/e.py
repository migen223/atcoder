from heapq import *
n,m,k=map(int,input().split())
graph=[[] for _ in range(n+1)]
secu=[]

for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(k):
    p,h=map(int,input().split())
    secu.append((p,h))

vis=[-1]*(n+1)
hq=[]
for p,h in secu:
    vis[p]=h
    heappush(hq,(-h,p))

while hq:
    h,now=heappop(hq)
    h*=-1
    #print("h,now",h,now)
    if vis[now]==h:
        for ne in graph[now]:
            if vis[ne]<h-1:
                vis[ne]=h-1
                if h-1>0:
                    heappush(hq,(-(h-1),ne))

ans=[]
for i in range(1,n+1):
    if vis[i]>=0:
        ans.append(i)
ans.sort()
print(len(ans))
print(*ans)
