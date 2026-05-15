
n,k,t=map(int,input().split())

ans=0
for i in range(n):
    d,r=map(int,input().split())
    if r>=k*d:
        ans+=r

if ans>=t:
    print("Yes")
else:
    print("No")