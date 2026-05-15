n,k=map(int,input().split())
s=list(map(int,input().split()))
ans=0
for i in range(n):
    if s[i]>=k:
        ans+=1
print(ans)