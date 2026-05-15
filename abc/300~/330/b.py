n,l,r=map(int,input().split())
a=list(map(int,input().split()))
for i in range(n):
    if l<=a[i]<=r:
        print(a[i],end=" ")
    elif abs(l-a[i])>abs(r-a[i]):
        print(r,end=" ")
    else:
      print(l,end=" ")
print()