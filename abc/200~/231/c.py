from bisect import bisect_left
n,q=map(int,input().split())

a=list(map(int,input().split()))
a.sort()
for i in range(q):
    x=int(input())
    ind=bisect_left(a,x)
    print(n-ind)
