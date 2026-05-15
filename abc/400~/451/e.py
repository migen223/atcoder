import sys
n=int(input())

graph=[[] for i in range(n)]
leng=[[0 for _ in range(n)] for _ in range(n)]
for i in range(n-1):
    a=list(map(int,input().split()))
    for j in range(len(a)):
        leng[i][i+j+1]=a[j]
        leng[i+j+1][i]=a[j]

#print(leng)

for i in range(1,n):
    cand=[]
    for j in range(n):
        if i==j:
            continue
        #print("i",i,"j",j)
        #print(leng[0][j],leng[j][i],leng[0][i])
        if leng[0][j]+leng[j][i]==leng[0][i]:
            #print("i",i,"j",j)
            #print(leng[0][j],leng[j][i],leng[0][i])
            cand.append((j,leng[i][j]))
    edge=min(cand,key=lambda x:x[1])
    #print(min(cand,key=lambda x:x[1]))
    graph[i].append(edge)
    graph[edge[0]].append((i,edge[1]))

#print("graph")
#print(graph)


for i in range(n):
    vis=[-1]*n
    w=0
    vis[i]=0
    v=[i]
    while v:
        now=v.pop()
        for ne,w in graph[now]:
            if vis[ne]==-1:
                vis[ne]=vis[now]+w
                v.append(ne)
    for j in range(n):
        if vis[j]!=leng[i][j]:
            print("No")
            sys.exit()

print("Yes")