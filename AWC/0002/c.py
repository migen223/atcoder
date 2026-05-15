
n,m=map(int,input().split())
ans=0
for _ in range(n):
    a,b=map(int,input().split())
    if m>=a:
        if (m-a)%b==0:
            ans=max(ans,(m-a)//b)
        else:
            ans=max(ans,(m-a)//b+1)
print(ans)