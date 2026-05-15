
n=int(input())

ans=[-1,-1]
l=0
r=n+1
while r-l>1:
    mid=(l+r)//2
    print("?",1,n,1,mid)
    t=int(input())
    if t==mid:
        l=mid
    else:
        r=mid
ans[1]=l+1
l=0
r=n+1
while r-l>1:
    mid=(l+r)//2
    print("?",1,mid,1,n)
    t=int(input())
    if t==mid:
        l=mid
    else:
        r=mid
ans[0]=l+1
print("!",ans[0],ans[1])