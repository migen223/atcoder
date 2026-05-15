
n,x=map(int,input().split())
a=list(map(int,input().split()))
need=0
for i in range(n):
    if i%2==0:
        need+=a[i]
    else:
        need+=a[i]-1
if need<=x:
    print("Yes")
else:
    print("No")