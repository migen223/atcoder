from bisect import bisect_left
n=int(input())

l=[5*i for i in range(21)]
ind=bisect_left(l,n)
if ind==0:
    print(0)
else:
    if abs(l[ind]-n)<abs(n-l[ind-1]):
        print(l[ind])
    else:
        print(l[ind-1])
