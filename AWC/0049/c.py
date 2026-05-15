from bisect import bisect_right
n,k=map(int,input().split())
a=list(map(int,input().split()))
r=[0]
for i in range(n):
    r.append(r[-1]+a[i])

ans=0
for i in range(1,n+1):
    ind=bisect_right(r,r[i-1]+k)
    ans+=max(0,ind-i)
    
print(ans)


"""
0 1 3 6 10 15


"""