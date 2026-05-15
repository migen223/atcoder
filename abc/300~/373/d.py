from collections import deque
n,m=map(int,input().split())
graph=[[] for i in range(n+1)]

ans=[0]*(n+1)
for i in range(m):
    u,v,w=map(int,input().split())
    graph[u].append((v,w))
    graph[v].append((u,-w))

visit=[0]*(n+1)

for i in range(1,n+1):
    if visit[i]==0:
        visit[i]=1
        visitable=deque([(i,0)])
        while visitable:
            now=visitable.popleft()
            pos=now[0]
            w=now[1]
            ans[pos]=w
            #print(pos,w)
            for j in range(len(graph[pos])):
                if visit[graph[pos][j][0]]==0:
                    visit[graph[pos][j][0]]=1
                    visitable.append((graph[pos][j][0],w+graph[pos][j][1]))


for i in range(1,n+1):
    print(ans[i],end=" ")
print()