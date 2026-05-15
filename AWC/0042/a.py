
n,k=map(int,input().split())

ans=0
for i in range(n):
    a,b=map(int,input().split())
    if (a+b)%k==0:
        ans+=(a+b)//k
    else:
        ans+=(a+b)//k+1

print(ans)