from random import randint

alp=[]
for i in range(97, 123):
    alp.append(chr(i))

for _ in range(1000):
    n,q=randint(4,10),randint(4,10)
    col="a"
    tile=[0]*n
    end={}
    keep={}
    no=set([range(n)])
    f=0
    cl=["a"]*n
    ans1=["a"]*n
    query=[]
    for _ in range(q):
        z=[]
        que=[randint(1,2),-1]
        z.append(que[0])
        if que[0]=="1":
            x=randint(1,n)
            z.append(x)
            if tile[x]==0:
                no.discard(x)
                if x in keep:
                    end[x]=keep[x]
                    keep.pop(x)
                else:
                    end[x]=col
                tile[x]=1
            else:   
                keep[x]=end[x]
                end.pop(x)
                tile[x]=0
                no.add(x)
        else:
            f+=1
            c=alp[randint(0,23)]
            z.append(c)
            col=c
            keep={}
            for i in range(n):
                if tile[i]==0:
                    ans1[i]=c
        query.append(z)
    ans=[]
    for i in range(n):
        if i not in end:
            ans.append(col)
        else:
            ans.append(end[i])
    if "".join(ans)!="".join(ans1):
        print(n,q)
        print(query)
