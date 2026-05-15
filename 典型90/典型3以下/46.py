n=int(input())
i=input()
an=list(map(int,i.split()))
i=input()
bn=list(map(int,i.split()))
i=input()
cn=list(map(int,i.split()))
al=[0]*46
bl=[0]*46
cl=[0]*46
ans=0
for a in an:
    al[a%46]+=1
for b in bn:
    bl[b%46]+=1
for c in cn:
    cl[c%46]+=1
for i in range(46):
    for j in range(46):
        for k in range(46):
            if (i+j+k)%46==0:
                ans+=al[i]*bl[j]*cl[k]
print(ans)



