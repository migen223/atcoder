
n,m=map(int,input().split())
e=list(map(int,input().split()))
c=list(map(int,input().split()))
mi=min(e)
ans=0
for i in range(m):
    ans+=mi*c[i]
print(ans)