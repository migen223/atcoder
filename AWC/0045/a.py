
n=int(input())
ans=0
for i in range(n):
    t,p=input().split()
    p=int(p)
    if t=="normal":
        ans+=p
    else:
        ans+=p//2

    
print(ans)