from bisect import bisect_right
n,k=map(int,input().split())
a=list(map(int,input().split()))
r=[0]
for i in range(n):
    r.append(r[-1]+a[i])
ans=0

for i in range(n+1):
    ind=bisect_right(r,k+r[i])
    ans=max(ans,ind-i-1)
    #print(ind-i-1)

print(ans)