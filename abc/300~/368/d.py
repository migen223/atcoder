from collections import deque
n,k=map(int,input().split())
graph=[set() for i in range(n)]
for i in range(n-1):
    a,b=map(lambda x:int(x)-1,input().split())
    graph[a].add(b)
    graph[b].add(a)

v=set(map(lambda x:int(x)-1,input().split()))

l=[]
for i in range(n):
    if len(graph[i])==1 and i not in v:
        l.append(i)
ans=n
while l:
    now=l.pop()
    if now in v:
        continue
    nv=graph[now].pop()
    graph[nv].remove(now)
    ans-=1
    if len(graph[nv])==1:
        l.append(nv)
print(ans)
"""
visit=[-1]*n
visitable=[(0,0)]
visit[0]=0
while visitable:
    now=visitable.pop()
    pos=now[0]
    depth=now[1]
    for i in range(len(graph[pos])):
        if visit[graph[pos][i]]==-1:
            visit[graph[pos][i]]=depth+1
            visitable.append((graph[pos][i],depth+1))
check=[0]*n

ans=1
mind=min([visit[v[i]] for i in range(k)])


visitable=[v[i] for i in range(k)]
visitable.sort(key=lambda x:visit[x],reverse=True)
visitable=deque(visitable)
for i in range(k):
    if visit[visitable[-i-1]]==mind:
        check[visitable[-1-i]]=1
    else:
        break
while visit[visitable[0]]>mind:
    now=visitable.popleft()
    depth=visit[now]
    for i in range(len(graph[now])):
        if check[graph[now][i]]==0 and depth>visit[graph[now][i]]:
            check[graph[now][i]]=1
            if visit[graph[now][i]]==mind:
                visitable.append(graph[now][i])
                ans+=1
            else:
             visitable.appendleft(graph[now][i])
                ans+=1
        elif check[graph[now][i]]==1 and depth>visit[graph[now][i]]:
            ans+=1


while len(visitable)>1:
    l=[]
    while visitable:
        now=visitable.pop()
        depth=visit[now]
        for i in range(len(graph[now])):
            if check[graph[now][i]]==0 and depth>visit[graph[now][i]]:
                l.append(graph[now][i])
                check[graph[now][i]]=1
                ans+=1
            elif check[graph[now][i]]==1 and depth>visit[graph[now][i]]:
                ans+=1
    for i in l:
        visitable.append(i)

print(ans)
"""





