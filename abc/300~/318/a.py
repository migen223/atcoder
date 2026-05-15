n,m,p=map(int,input().split())

ans=0
k=0
for i in range(1,n+1):
    if m+p*k==i:
        ans+=1
        k+=1
print(ans)