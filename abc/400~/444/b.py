
n,k=map(int,input().split())

ans=0
for i in range(1,n+1):
    s=str(i)
    res=0
    for j in s:
        res+=int(j)
    if res==k:
        ans+=1
print(ans)