
x,y,n=map(int,input().split())

ans=0
if y/3<=x:
    ans+=(n//3)*y
    n-=(n//3)*3
    ans+=n*x
    print(ans)
else:
    print(x*n)