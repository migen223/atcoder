
n,q=map(int,input().split())
c=list(map(int,input().split()))
toind={}
ans=[]
for i in range(n):
    toind[i]=i
    ans.append(set([c[i]]))

for _ in range(q):
    a,b=map(lambda x:int(x)-1,input().split())
    an=len(ans[a])
    bn=len(ans[b])
    if an<=bn:
        for ai in ans[a]:
            ans[b].add(ai)
        ans[a]=set()
    else:
        for bi in ans[b]:
            ans[a].add(bi)
        ans[b]=set()
        ans[a],ans[b]=ans[b],ans[a]
    print(len(ans[b]))


"""
setl=[frozenset()]
dic={}
dic[frozenset([])]=0
ind=1
for i in range(n):
    s=frozenset([c[i]])
    if s not in dic:
        dic[s]=ind
        setl.append(s)
        ind+=1
#print(dic)
#print(setl)
ans=[]
for i in range(n):
    ans.append(dic[frozenset([c[i]])])   
#print(ans)

for _ in range(q):
    a,b=map(lambda x:int(x)-1,input().split())
    if ans[a]==ans[b]:
        print(len(setl[ans[a]]))
        ans[a]=0
        continue
    next=setl[ans[a]]|setl[ans[b]]
    if next not in dic:
        dic[next]=ind
        setl.append(next)
        ind+=1
    ans[a]=0
    ans[b]=dic[next]
    print(len(setl[ans[b]]))
    #print(ans)
    #print(dic)
    #print(setl)
   #print()
    
"""