
n,k=map(int,input().split())

ans=0
for i in range(n):
    s=input()
    res=0
    for si in s:
        if si=="!":
            res+=1
    if res>=k:
        ans+=1

print(ans)