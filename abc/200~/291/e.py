import sys
n,m=map(int,input().split())
graph=[set() for i in range(n+1)]
rgraph=[set() for i in range(n+1)]
for _ in range(m):
    x,y=map(int,input().split())
    if y not in rgraph[x]:
        rgraph[x].add(y)
    if x not in graph[y]:
        graph[y].add(x)
    
rel=[]
f=0
count=[len(graph[i]) for i in range(n+1)]
visitable=[]
for i in range(1,n+1):
    if len(graph[i])==0:
        visitable.append(i)
while visitable:
    if len(visitable)>=2:
        print("No")
        sys.exit()
    now=visitable.pop()
    rel.append(now)
    for ne in rgraph[now]:
        count[ne]-=1
        if count[ne]==0:
            visitable.append(ne)
#print(rel)
if len(rel)<n:
    print("No")
else:
    ans=[0]*n
    for i in range(1,n+1):
        ans[rel[i-1]-1]=i
    print("Yes")
    print(*ans)
