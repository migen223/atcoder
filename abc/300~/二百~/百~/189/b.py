import sys
n,x=map(int,input().split())
now=0
x*=100
for i in range(n):
    v,p=map(int,input().split())
    now+=v*p
    if now>x:
        print(i+1)
        sys.exit()

print(-1)