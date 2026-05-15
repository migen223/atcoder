from collections import deque
n=int(input())
c=list(map(int,input().split()))
a=list(map(int,input().split()))
dist=[10**32]*(n)
dist[0]=0
for i in range(1,n):
    for j in range(1,c[i-1]+1):
        if 0<=i-j<=n-1:
            dist[i]=min(dist[i],dist[i-j]+1)

graph=[[] for i in range(n)]
for i in range(n-1):
    for j in range(1,c[i]+1):
        #print(i+1,j,c[i],i+1-j)
        if 0<=i+1-j<=n:
            graph[i+1].append(i+1-j)

def count(l,r):
    vis=[-1]*(r+1)
    v=deque([(r,0)])
    vis[r]=0
    while v:
        pos,d=v.popleft()
        for ne in graph[pos]:
            if vis[ne]==-1:
                vis[ne]=d+1
                v.append((ne,d+1))
                if ne==l:
                    return d+1             

beans=[]
for i in range(n-1):
    if a[i]>0:
        beans.append(i+1)

ans=0
while len(beans)>=2:
    now=beans.pop()
    ans+=count(beans[-1],now)
ans+=dist[beans[0]]
print(ans)



            
