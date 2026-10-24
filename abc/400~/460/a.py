n,m=map(int,input().split())

ans=0
while True:
    m=n%m
    ans+=1
    if m==0:
        break
print(ans)