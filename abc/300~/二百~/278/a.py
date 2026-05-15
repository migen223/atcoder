n,k=map(int,input().split())
a=list(map(int,input().split()))
for i in range(k):
    a.append(0)
for i in range(n):
    print(a[i+k],end=" ")
print()