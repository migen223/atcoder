import sys
n,m=map(int,input().split())
f=list(map(int,input().split()))
c=[0]*m
for i in range(n):
    c[f[i]-1]+=1
s=set(f)
if len(s)==n:
    print("Yes")
else:
    print("No")


for i in range(m):
    if c[i]==0:
        print("No")
        sys.exit()

print("Yes")
