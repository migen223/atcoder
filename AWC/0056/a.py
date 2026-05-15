
n,m=map(int,input().split())
a=list(map(int,input().split()))
ans=0
for  i in range(m):
    b,s=map(int,input().split())
    ans+=a[b-1]+s

print(ans)
