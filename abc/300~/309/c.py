
n,k=map(int,input().split())

kikan=[]
medi=[]
dic={}
se=set()
for i in range(n):
    a,b=map(int,input().split())
    kikan.append(a)
    medi.append(b)
    if a in se:
        dic[a].append(b)
    else:
        dic[a]=[b]
        se.add(a)
#print(dic)
kikan.sort()
now=sum(medi)
l=list(se)
l.sort()
if now<=k:
    print(1)
else:
    for i in l:
        #print(now,sum(dic[i]))
        if now-sum(dic[i])<=k:
            print(i+1)
            break
        else:
            now-=sum(dic[i])