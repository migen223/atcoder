from collections import deque
n=int(input())
graph=[[] for i in range(n+1)]
for i in range(n-1):
    a,b=map(int,input().split())
    if a!=b:
        graph[a].append(b)
        graph[b].append(a)

for i in range(1,n+1):
    graph[i]=deque(sorted(graph[i]))

visit=[0]*(n+1)
visit[1]=1

visitable=[[graph[1][0],1,1]]
#print(graph)
print(1,end=" ")
k=0
while visitable :
    now=visitable.pop()
    nowp=now[0]
    pre=now[1]
    if now[2]==1:
       visit[nowp]=pre
    print(nowp,end=" ")
    f=0
    for i in range(len(graph[nowp])):
        if visit[graph[nowp][i]]==0:
            f+=1
            visitable.append([graph[nowp][i],nowp,1])
            graph[nowp].popleft()
            break
    if f==0:
        if nowp==1:
            visitable=[]
        else:
            visitable.append([visit[nowp],nowp,0])
    #print(visitable)
    #print(visit)
print()
