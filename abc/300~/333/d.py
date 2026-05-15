
n=int(input())

graph=[[] for i in range(n)]

for i in range(n-1):
    u,v=map(lambda x:int(x)-1,input().split())
    graph[u].append(v)
    graph[v].append(u)

if len(graph[0])==1:
    print(1)
else:
    ans=1
    visit=[0]*n
    visit[0]=1
    visitable=[(0,-1)]
    count=0
    ansl=[0]*len(graph[0])
    while visitable:
        now=visitable.pop()
        pos=now[0]
        id=now[1]
        for ne in graph[pos]:
            if visit[ne]==0 :
                if id==-1:
                    visitable.append((ne,count))
                    ansl[count]=1
                    count+=1
                    visit[ne]=1
                else:
                    visitable.append((ne,id))
                    ansl[id]+=1
                    visit[ne]=1
    ansl.sort(reverse=True)
    while len(ansl)>=2:
        ans+=ansl[-1]
        ansl.pop()
    print(ans)
                    
                
