
p,q=map(int,input().split())
x,y=map(int,input().split())

if p+99>=x>=p and q+99>=y>=q :
    print("Yes")
else:
    print("No")