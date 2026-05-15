
n,x=map(int,input().split())
a=list(map(int,input().split()))

for i in range(n):
    if a[i]<x:
        print(1)
        x=a[i]
    else:
        print(0)