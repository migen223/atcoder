n,m=map(int,input().split())
graph=[[] for _ in range(n)]
for i in range(m):
    v1,v2=map(int,input().split())
    graph[v1-1].append(v2-1)
    graph[v2-1].append(v1-1)

def countc(g,visit):
    count=0
    for start in range(n):
        if visit[start]==0:
            stack=[start]
            visit[start]=1 #1が行ったやつ
            while stack:
                dist=stack.pop()
                visit[dist]=1
                for to in g[dist]:
                    if visit[to]==0:
                        stack.append(to)
            count+=1
    return count 

visit=[0]*n
print(m-n+countc(graph,visit))
