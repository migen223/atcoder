from bisect import bisect_left
n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
p=998244353

a.sort()
b.sort()
ans=0
r=[0]
for i in range(m):
    r.append(r[-1]+b[i])

for i in range(n):
    ind=bisect_left(b,a[i])
    if ind==0:
        ans+=r[-1]-m*a[i]
    elif ind==m:
        ans+=m*a[i]-r[-1]
    else:
        ans+=(ind)*a[i]-r[ind]
        ans+=(r[-1]-r[ind])-(m-ind)*a[i]
    ans%=p
print(ans)


