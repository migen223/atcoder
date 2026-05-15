
n,k=map(int,input().split())

ans=0
for i in range(n):
    a=list(map(int,input().split()))
    for j in range(1,len(a)):
        if a[j]>=k:
            ans+=1

print(ans)
