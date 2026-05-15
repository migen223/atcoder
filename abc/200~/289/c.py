from itertools import product
n,m=map(int,input().split())
sg=[set() for i in range(m)]

for i in range(m):
    c=int(input())
    l=list(map(int,input().split()))
    for j in range(c):
        sg[i].add(l[j])
    
ans=0
need=set(range(1,n+1))
for p in product([0,1],repeat=m):
    se=set()
    l=list(p)
    for i in range(m):
        if l[i]==1:
            se=se|sg[i]
    if need<=se:
        ans+=1
print(ans)


