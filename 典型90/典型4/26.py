n=int(input())
graph=[[] for i in range(n+1)]
for i in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

#print(graph)
checkl=[]
visit=set()
deep=0
visitable=[[1,0]]
while visitable:
    now=visitable.pop()
    checkl.append(now)
    visit.add(now[0])
    for i in graph[now[0]]:
        if i not in visit:
            visitable.append([i,now[1]+1])
    #print(visitable)

even=[]
odd=[]
for i in range(n):
    if checkl[i][1]%2==0:
        odd.append(checkl[i][0])
    else:
        even.append(checkl[i][0])
if len(even)>=len(odd):
    for i in range(n//2):
        print(even[i],end=" ")
else:
    for i in range(n//2):
        print(odd[i],end=" ")
