
n,m,k=map(int,input().split())
s=list(map(int,input().split()))

for i in range(m):
    p,v=map(int,input().split())
    s[p-1]=v

ans=0
for i in s:
    if i<k:
        ans+=1

print(ans)