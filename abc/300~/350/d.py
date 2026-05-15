
n,m=map(int,input().split())

graph=[[] for i in range(n+1)]

for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visit=[0]*(n+1)

ren=[]
for i in range(1,n+1):
    if visit[i]==0:
        mi=(len(graph[i]),i)
        count=1
        visitable=[i]
        visit[i]=1
        while visitable:
            now=visitable.pop()
            for  nxt in graph[now]:
                if visit[nxt]==0:
                    visit[nxt]=1
                    count+=1
                    visitable.append(nxt)
        ren.append(count)
ans=0
for i in ren:
    ans+=(i*(i-1))//2
ans-=m
print(ans)


