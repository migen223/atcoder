
n,k=map(int,input().split())
a=list(map(int,input().split()))
for i in range(n):
    print(a[(i+(n-k))%n],end=" ")
print()