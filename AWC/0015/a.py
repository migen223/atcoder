a=list(map(int,input().split()))
b=list(map(int,input().split()))
ans=0
for i in range(7):
    ans+=a[i]*b[i]
print(ans)