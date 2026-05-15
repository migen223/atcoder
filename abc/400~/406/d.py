
h,w,n=map(int,input().split())

g=[]
dicx={}
dicy={}
gset=set()
for i in range(n):
    x,y=map(int,input().split())
    if x in dicx:
        dicx[x].append(i)
    else:
        dicx[x]=[i]
    if y in dicy:
        dicy[y].append(i)
    else:
        dicy[y]=[i]
    gset.add(i)

#print(dicx)
#print(dicy)

q=int(input())
for _ in range(q):
    ans=0
    que=list(map(int,input().split()))
    if que[0]==1:
        x=que[1]
        if x in dicx:
            for i in dicx[x]:
                if i in gset:
                    ans+=1
                    gset.remove(i)
            dicx.pop(x)
    else:
        y=que[1]
        if y in dicy:
            for i in dicy[y]:
                if i in gset:
                    ans+=1
                    gset.remove(i)
            dicy.pop(y)
    #print(gset)
    print(ans)