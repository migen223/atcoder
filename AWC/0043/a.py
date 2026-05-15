from math import floor
n,m=map(int,input().split())
a=list(map(int,input().split()))

for i in range(n):
    m=m*a[i]//100
print(m)