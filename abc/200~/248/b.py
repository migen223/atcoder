
a,b,k=map(int,input().split())
now=a
ans=0
while now<b:
    now*=k
    ans+=1
print(ans)