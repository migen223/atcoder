n,q=map(int,input().split())
nest=[1]*n
bird=[i for i in range(n)]
ans=0
for i in range(q):
    que=input().split()
    if len(que)==3:
        b=int(que[1])-1
        ne=int(que[2])-1
        if nest[ne]==1:
            ans+=1
        if nest[bird[b]]==2:
            ans-=1
        nest[bird[b]]-=1
        nest[ne]+=1
        bird[b]=ne
    else:
        print(ans)