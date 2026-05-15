from bisect import *
n,m,d=map(int,input().split())
a=sorted(list(map(int,input().split())))
b=sorted(list(map(int,input().split())))
b.insert(0,-10**9)

ans=-1

for i in range(n):
    r=bisect_right(b,a[i]+d)-1
    l=bisect_left(b,a[i]-d)
    #print(l,r,a[i])
    if abs(a[i]-b[r])<=d:
        ans=max(ans,a[i]+b[r])
    if l!=m+1:
        if abs(a[i]-b[l])<=d:
            ans=max(ans,a[i]+b[l])

print(ans)
