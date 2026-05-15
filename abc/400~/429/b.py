import sys
n,m=map(int,input().split())
a=list(map(int,input().split()))

s=sum(a)

for i in range(n):
    if s-a[i]==m:
        print("Yes")
        sys.exit()

print("No")