
n,s,c=map(int,input().split())

ans=0
for i in range(n):
    h,p=map(int,input().split())
    if s>=h:
        s+=-h+p
    else:
        ans+=c

print(ans)
