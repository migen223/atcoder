from bisect import bisect_right
n,m,k=map(int,input().split())
h=list(map(int,input().split()))
b=list(map(int,input().split()))

r=n-1

ans=0

h.sort()
b.sort(reverse=True)
#print(h)
#print(b)

for i in range(m):
    ind=bisect_right(h,b[i])
    #print(ind)
    if ind==0:
        break
    while len(h)>=1 and len(h)!=ind-1:
        h.pop()
    ans+=1
    if len(h)==0:
        break

if ans>=k:
    print("Yes")
else:
    print("No")

