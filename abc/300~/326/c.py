from bisect import bisect_left
n,m=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
ans=0
for i in range(n):
    r=bisect_left(a,a[i]+m)
    ans=max(ans,r-i)
print(ans)