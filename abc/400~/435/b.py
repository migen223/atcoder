
n=int(input())
a=list(map(int,input().split()))

ans=0

for l in range(n-1):
    for r in range(l,n):
        now=0
        for k in range(l,r+1):
            now+=a[k]
        f=0
        for k in range(l,r+1):
            if now%a[k]==0:
                f+=1
                break
        if f==0:
            ans+=1
print(ans)

