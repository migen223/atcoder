from collections import deque
n,q=map(int,input().split())
graph=[[] for i in range(n+1)]
for i in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

depth=[-1]*(n+1)
depth[1]=0
visitable=deque([1])
while visitable:
    now=visitable.popleft()
    for i in range(len(graph[now])):
        if depth[graph[now][i]]==-1:
            depth[graph[now][i]]=depth[now]+1
            visitable.append(graph[now][i])
#print(depth)

for i in range(q):
    c,d=map(int,input().split())
    if abs(depth[c]-depth[d])%2==1:
        print("Road")
    else:
        print("Town")


#for i in range(q):


