n,p,q,r,s=map(int,input().split())
a=list(map(int,input().split()))

ans=[]
l=a[p-1:q]
right=a[r-1:s]
for i in range(n):
    if p-1<=i<=q-1:
        ans.append(right.pop(0))
    elif r-1<=i<=s-1:
        ans.append(l.pop(0))
    else:
        ans.append(a[i])
print(*ans)
