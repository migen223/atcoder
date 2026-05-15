
n,q=map(int,input().split())

node={}
for i in range(1,n+1):
    node[i]=set()
ans=n
for _ in range(q):
    que=list(map(int,input().split()))
    if que[0]==1:
        u,v=que[1],que[2]
        if len(node[u])==0:
            ans-=1
        if len(node[v])==0:
            ans-=1
        node[u].add(v)
        node[v].add(u)
    elif que[0]==2:
        v=que[1]
        if len(node[v])>=1:
            ans+=1
        for i in node[v]:
            node[i].remove(v)
            if len(node[i])==0:
                ans+=1
        node[v]=set()
    print(ans)

