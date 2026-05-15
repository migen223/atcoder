from bisect import *
n=int(input())
a=list(map(int,input().split()))
ansl=[]
for i in range(n):
    ind=bisect_left(a,a[i]*2)
    if ind!=n:
        ansl.append(n-ind)

print(sum(ansl))