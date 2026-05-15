
n=int(input())
p=list(map(int,input().split()))

ans=0
graph=[[] for i in range(n+1)]
for i in range(n):
    graph[p[i]].append(i+1)
    graph[i+1].append(p[i])

ans=0
visit=[0]*(n+1)
for i in range(1,n+1):
    if visit[i]==0:
        res=0
        visitable=[i]
        visit[i]=1
        while visitable:
            res+=1
            now=visitable.pop()
            for ne in graph[now]:
                if visit[ne]==0:
                    visit[ne]=1
                    visitable.append(ne)
        if res>=2:
            ans+=(res*(res-1))//2
print(ans)
