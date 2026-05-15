
n,m=map(int,input().split())
s=list(map(int,input().split()))

imos=[0]*(n+1)
for i in range(m):
    l,r,w=map(int,input().split())
    l-=1
    imos[l]+=w
    imos[r]-=w

for i in range(1,n):
    imos[i]+=imos[i-1]

ans=0
for i in range(n):
    if imos[i]>s[i]:
        ans+=1

print(ans)
