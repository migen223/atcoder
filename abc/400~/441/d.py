from collections import deque
n,m,l,s,t=map(int,input().split())

graph=[[] for i in range(n)]

for i in range(m):
    u,v,c=map(lambda x:int(x)-1,input().split())
    c+=1
    graph[u].append((v,c))
#print(graph)
ans=set()
visitable=deque([[0,0,0]])
while visitable:
    pos,cost,move=visitable.popleft()

    if move==l:
        if s<=cost<=t:
            ans.add(pos+1)
    else:
        for ne in graph[pos]:
            visitable.append([ne[0],cost+ne[1],move+1])
    #print(visitable)

ans=list(ans)
ans.sort()
print(*ans)

