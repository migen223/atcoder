from collections import deque
n=int(input())
p=list(map(lambda x:int(x)-1,input().split()))
w=list(map(int,input().split()))

graph=[[] for i in range(n)]
rgraph=[[] for i in range(n)]

for i in range(n-1):
    graph[p[i]].append(i+1)
    rgraph[i+1].append(p[i])

leaf=deque([])
count=[0]*n
num=[0]*n
for i in range(1,n):
    if len(graph[i])==0:
        leaf.append(i)
for i  in range(n):
    num[i]+=w[i]
#print(leaf)
while leaf:
    now=leaf.popleft()
    for ne in rgraph[now]:
        count[ne]+=1
        num[ne]+=num[now]
        #print("ne",ne,num[ne])
        if count[ne]==len(graph[ne]):
            leaf.append(ne)

ans=0
for i in range(n):
    if len(graph[i])>=2:
        l=[]
        for e in graph[i]:
           l.append(num[e])
        ans=max(ans,max(l)-min(l))
print(ans)