
n,k=map(int,input().split())
a=list(map(int,input().split()))
def mysum(a0,an,d):
    n=(a0-an)//abs(d)+1
    return n*(a0+an)//2

def check(m):
    count=0
    for i in range(n):
        count+=max(0,a[i]-m+1)
    if count<=k:
        return True
    return False

s=0
for i in range(n):
    s+=mysum(a[i],0,-1)

if sum(a)<=k:
    print(s)
else:                    
    l=1
    r=2*10**9+1
    while r-l>1:
        m=(l+r)//2
        if check(m):
            r=m
        else:
            l=m
        #print(l,r)
    ans=0
    #print(r)
    for i in range(n):
        if a[i]>=r:
            ans+=mysum(a[i],r,-1)
            k-=a[i]-r+1
    ans+=k*(r-1)
    print(ans)

