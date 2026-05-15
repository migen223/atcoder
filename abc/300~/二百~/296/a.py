import sys
n,x=map(int,input().split())
a=list(map(int,input().split()))
se=set(a)
for i in range(n):
    if x+a[i] in se:
        print("Yes")
        sys.exit()

print("No")
        