
n,k=map(int,input().split())
p=list(map(int,input().split()))
ans=0
for i in p:
    if i%k==0:
        ans+=i
print(ans)