
n=int(input())
a=list(map(int,input().split()))
graph=[[] for i in range(n+1)]
for i in range(n):
    graph[i+1].append(a[i])

visit=[-1]*(n+1)
ans=[-1]*(n+1)
for i in range(1,n+1):
    if visit[i]==-1:
        visitable=[i]
        res=[i]
        goal=-1
        while visitable:
            now=visitable.pop()
            for ne in graph[now]:
                if visit[ne]==-1:
                    visit[ne]=1
                    visitable.append(ne)
                    res.append(ne)
                else:
                    goal=ans[ne]

                if now==ne:
                    goal=ne
        for j in res:
            ans[j]=goal
        #print(res,goal)

for i in range(1,n+1):
    print(ans[i],end=" ")
print()
        
#11 14 14 14 15 14 14 11 11 14 11 12 14 14 15
#11 14 14 14 15 14 14 11 11 14 11 12 14 14 15 