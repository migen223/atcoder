from bisect import bisect_left
n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
b.sort()
ans=10**9

for i in range(n):
    ind=bisect_left(b,a[i])
    for j in [0,-1]:
        nm=ind+j
        if 0<=nm<=m-1:
            ans=min(ans,abs(a[i]-b[nm]))
print(ans)

