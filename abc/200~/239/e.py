
n,q=map(int,input().split())
x=list(map(int,input().split()))

dic={}
for i in range(1,n+1):
    dic[i]=x[i-1]

graph=[[] for _ in range(n+1)]
for i in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

query=[]
for i in range(q):
    v,k=map(int,input().split())
    query.append((v,k))

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

kl=[[] for i in range(n+1)]
for i in range(1,n+1):
    kl[i].append(dic[i])

visit=[0]*(n+1)
visitable=[leafs[i] for i in range(len(leafs))]


while visitable:
    now=visitable.pop()
    #print("now",now)
    if len(rgraph[now])==0:
        kl[now].sort(reverse=True)
        while len(kl[now])>20:
            kl[now].pop()
        break
    ne=rgraph[now][0]
    for ki in kl[now]:
        kl[ne].append(ki)
    visit[ne]+=1
    if visit[ne]==len(ngraph[ne]):
        kl[ne].sort(reverse=True)
        while len(kl[ne])>20:
            kl[ne].pop()
            #print("kl",kl[ne],len(kl[ne]),k)
        visitable.append(ne)
    #print(kl)
    #print("ne",ne,now)
#print(kl)
for que in query:
    v,k=que
    print(kl[v][k-1])
