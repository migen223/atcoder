import sys
n,k=map(int,input().split())
p=list(map(int,input().split()))

for i in range(n):
    if p[i]>=k:
        print(i+1)
        sys.exit()

print(-1)