
n,m=map(int,input().split())
graph=[[] for i in range(n)]

for i in range(m):
    a,b,c=map(int,input().split())
    a-=1
    b-=1
    graph[a].append([b,c])
    graph[b].append([a,c])


#print(graph)
ans=0

for i in range(n):
    visit=[False]*n
    visitable=[[i,0,visit]]
    while visitable:
        now=visitable.pop()
        now[2][now[0]]=True
        ans=max(ans,now[1])
        #print(now[0],now[1],now[2])
        for j in range(len(graph[now[0]])):
            if not now[2][graph[now[0]][j][0]]:
                new_visit=now[2][:]
                visitable.append([graph[now[0]][j][0],now[1]+graph[now[0]][j][1],new_visit])

print(ans)



