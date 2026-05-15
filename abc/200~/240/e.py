from collections import deque
n=int(input())
graph=[[] for i in range(n+1)]
for _ in range(n-1):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

ngraph=[[] for i in range(n+1)]
rgraph=[[] for i in range(n+1)]
visit=[0]*(n+1)
visit[1]=1
visitable=[1]
leafs=[]
while visitable:
    now=visitable.pop()
    visit[now]=1
    if now!=1 and len(graph[now])==1:
        leafs.append(now)
    for ne in graph[now] :
        if visit[ne]==0:
            ngraph[now].append(ne)
            rgraph[ne].append(now)
            visit[ne]=1
            visitable.append(ne)
#print(ngraph)
#print(rgraph)
leafcount=[0]*(n+1)
for l in leafs:
    leafcount[l]+=1

visitable=deque([leafs[i] for i in range(len(leafs))])
visit=[0]*(n+1)
while visitable:
    now=visitable.popleft()
    if len(rgraph[now])>=1 :
        ne=rgraph[now][0]
        leafcount[ne]+=leafcount[now]
        if visit[ne]+1==len(ngraph[ne]):
            visitable.append(ne)
        else:
            visit[ne]+=1
        #print("ne",ne,now)
    #print("lc",leafcount)
    #print(visitable)
#print(list(range(n+1)))
#print(leafcount)
    
ansl=[[0,0] for i in range(n+1)]

visitable=deque([(1,1,leafcount[1])])
while visitable:
    pos,l,r=visitable.popleft()
    ansl[pos]=[l,r]
    b=l
    for ne in ngraph[pos]:
        visitable.append((ne,b,b+leafcount[ne]-1))
        b+=leafcount[ne]

for i in range(1,n+1):
    print(*ansl[i])