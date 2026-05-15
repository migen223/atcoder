
n=int(input())
a=list(map(int,input().split()))
for i in range(n):
    d=0
    for j in range(7):
        d+=a[i*7+j]
    print(d,end=" ")
print()