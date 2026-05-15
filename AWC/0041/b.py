from bisect import bisect_right
n,m=map(int,input().split())
w=list(map(int,input().split()))
b=list(map(int,input().split()))

wl=[0]
ma=0
for i in range(m-1):
    if w[i]>ma:
        ma=w[i]
    wl.append(ma)

for bi in b:
    print(bisect_right(wl,bi))
