n,k=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
ans=1000000000
for i in range(k+1):
    #print(i+n-k-1,i)
    ans=min(ans,a[i+n-k-1]-a[i])
print(ans)