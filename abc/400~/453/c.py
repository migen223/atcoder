from itertools import product
n=int(input())
l=list(map(int,input().split()))
ans=0


for p in product([-1,1],repeat=n):
    res=0
    now=0.5
    for i in range(n):
        ne=now+p[i]*l[i]
        if now*ne<0:
            res+=1
        now=now+p[i]*l[i]
        #print(now)
    ans=max(ans,res)
print(ans)