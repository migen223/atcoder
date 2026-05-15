from math import lcm
n,m,k=map(int,input().split())

l=0
r=10**32
lc=lcm(n,m)
if m%n==0 or n%m==0:
    while r-l>1:
        mid=(l+r)//2
        res=(mid//min(n,m)-mid//max(n,m))
        if res==k:
            #print(mid)
            ans=max(n*(mid//n),m*(mid//m))
            if ans%n==0 and ans%m==0:
                ans=max(n*((mid//n)-1),m*((mid//m)-1))
            print(ans)
            break
        elif res>k:
            r=mid
        else:
            l=mid
else:
    while r-l>1:
        mid=(l+r)//2
        res=(mid//n+mid//m-2*(mid//(lc)))
        if res==k:
            #print(mid)
            ans=max(n*(mid//n),m*(mid//m))
            if ans%n==0 and ans%m==0:
                ans=max(n*((mid//n)-1),m*((mid//m)-1))
            print(ans)
            break
        elif res>k:
            r=mid
        else:
            l=mid
        #print(mid,res)

"""
ans=[]
for i in range(1,k+1):
    if (i%n==0 and i%m!=0) or (i%n!=0 and i%m==0):
        ans.append(i)
print(len(ans))
print(ans)
"""
