import sys
n,k=map(int,input().split())
a=list(map(int,input().split()))
for i in range(n):
    if a[i]==k:
        print(i+1)
        sys.exit()
print(-1)