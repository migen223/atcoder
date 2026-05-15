
n,m=map(int,input().split())
c=list(map(int,input().split()))
ans=0
l=[0]*m
for i in range(n):
    a,b=map(int,input().split())
    l[a-1]+=b

for i in range(m):
    ans+=min(l[i],c[i])
print(ans)
