from bisect import *
n,q=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
sa=sum(a)
maxa=max(a)
ruiseki=[]
r=0
for i in a:
    r+=i
    ruiseki.append(r)
for i in range(q):
    b=int(input())
    ans=0
    if maxa<b:
        print(-1)
    else:
        ins=bisect_left(a,b)
        if ins!=0:
            ans=ruiseki[ins-1]
        else:
            ans=0
        ans+=(n-ins)*(b-1)+1
        print(ans)

