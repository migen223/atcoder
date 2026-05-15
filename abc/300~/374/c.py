from itertools import *
n=int(input())
k=list(map(int,input().split()))
ans=n*100000000
for p in product([0,1],repeat=n):
    g0=0
    g1=0
    for i in range(n):
        if p[i]==1:
           g0+=k[i]
        else:
           g1+=k[i]  
    big=max(g0,g1)
    ans=min(big,ans)
print(ans)