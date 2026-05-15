a=list(map(int,input().split()))

two=[]
k=1
for i in range(64):
    two.append(k)
    k*=2
ans=0
for i in range(64):
    ans+=a[i]*two[i]
print(ans)
