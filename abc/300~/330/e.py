from sortedcontainers import SortedSet
from collections import Counter
n,q=map(int,input().split())
a=list(map(int,input().split()))
mexs=SortedSet([])
c=Counter(a)


for i in range(n+1):
    if i not in c:
        mexs.add(i)

for _ in range(q):
    i,x=map(int,input().split())
    i-=1
    if c[a[i]]==1:
        c.pop(a[i])
        if a[i]<=n:
            mexs.add(a[i])
    else:
        c[a[i]]-=1
    if x in c:
        c[x]+=1
    else:
        c[x]=1
        if x<=n:
            mexs.remove(x)
    a[i]=x
    print(mexs[0])
