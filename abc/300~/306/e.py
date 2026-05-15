from sortedcontainers import SortedList
n,k,q=map(int,input().split())

ans=0
kd={}
kd[0]=k
ad={}
ad[0]=n
a=[0]*(n)
sla=SortedList([0]*n)
slk=SortedList([0]*k)


for _ in range(q):
    x,y=map(int,input().split())
    x-=1
    pre=a[x]
    ad[pre]-=1
    f=0
    if pre in kd:
        if kd[pre]>ad[pre]:
            kd[pre]-=1
            slk.discard(-pre)
            ans-=pre
            f+=1
        if kd[pre]==0:
            kd.pop(pre)
    if ad[pre]==0:
        ad.pop(pre)
    
    sla.discard(-pre)
    sla.add(-y)
    if y in ad:
        ad[y]+=1
    else:
        ad[y]=1

    if f==1:
        plus=-sla[k-1]
        ans+=plus
        slk.add(-plus)
        if plus in kd:
            kd[plus]+=1
        else:
            kd[plus]=1

    mi=-slk[k-1]
    if mi<y:
        slk.discard(-mi)
        slk.add(-y)
        kd[mi]-=1
        if kd[mi]==0:
            kd.pop(mi)
        if y in kd:
            kd[y]+=1
        else:
            kd[y]=1
        ans=ans-mi+y

    a[x]=y
    #print("a:",*a)
    #print("slk",slk,"\n","sla",sla)
    #print("ad",ad,"kd",kd)
    print(ans)


