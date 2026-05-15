import sys
from bisect import bisect_left
n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a.sort()
b.sort()
#print(a)
#print(b)
ind=0
ans=0
for i in range(m):
    if ind==n:
        print(-1)
        sys.exit()
    box=bisect_left(a,b[i],lo=ind)
    #print(box,ind)
    if box==n:
        print(-1)
        sys.exit()
    else:
        #print(box)
        ans+=a[box]
        ind=box+1
    
print(ans)


