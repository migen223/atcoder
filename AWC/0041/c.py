from bisect import bisect_left

n,k=map(int,input().split())
a=list(map(int,input().split()))
ans=0
a.sort()
for i in range(n-1):
    ans+=n-bisect_left(a,k-a[i],lo=i+1)
    #print(bisect_left(a,k-a[i],lo=i+1),a[i])
print(ans)