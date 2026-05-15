import sys
n,a,b=map(int,input().split())
d=list(map(int,input().split()))
w=a+b
d=list(set([d[i]%w for i in range(n)]))
d.sort()
size=len(d)
for i in range(len(d)):
    d.append(d[i]+w)

for i in range(size):
    if d[i+size-1]-d[i]+1<=a:
        print("Yes")
        sys.exit()

print("No")