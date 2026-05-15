
n,k=map(int,input().split())
a=list(map(int,input().split()))


now=0
for i in range(k):
    now+=a[i]
ans=0
if now<=0:
    ans+=1
for i in range(n-k):
    now-=a[i]
    now+=a[i+k]
    if now<=0:
        ans+=1

print(ans)