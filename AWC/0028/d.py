import heapq
n,m=map(int,input().split())

graph=[[] for i in range(n+1)]
rgraph=[[] for i in range(n+1)]
for _ in  range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    rgraph[b].append(a)

l=[]
flag=[0]*(n+1)
for i in range(1,n+1):
    if len(rgraph[i])==0:
        heapq.heappush(l,i)
        flag[i]+=1
#print(l)
ans=[]
while l:
    now=heapq.heappop(l)
    ans.append(now)
    #print(now,ans)
    for ne in graph[now]:
        flag[ne]+=1
        if flag[ne]==len(rgraph[ne]):
            heapq.heappush(l,ne)

print(*ans)