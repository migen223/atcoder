n,k,x=map(int,input().split())
a=list(map(int,input().split()))
b=[]
for i in range(n):
    if i==k:
        b.append(x)
    b.append(a[i])
if k==n:
    b.append(x)
print(*b)

