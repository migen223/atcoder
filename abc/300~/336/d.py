
n=int(input())
a=list(map(int,input().split()))
l=[0]*(n+1)
r=[0]*(n+1)
for i in range(1,1+n):
    l[i]=min(l[i-1]+1,a[i-1])
for i in range(n-1,-1,-1):
    r[i]=min(r[i+1]+1,a[i])
#print(l)
#print(r)
ans=-1
for i in range(n):
    ans=max(min(l[i+1],r[i]),ans)
print(ans)