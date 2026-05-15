from bisect import bisect_left
import sys
n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))



a.sort()
b.sort()

l=0
r=max(b)+1
def count(p):
    ca=0
    cb=0
    for i in range(n):
        if p>=a[i]:
            ca+=1
    for i in range(m):
        if p<=b[i]:
            cb+=1
    return ca>=cb

while r-l>1:
    mid=(r+l)//2
    if count(mid):
        r=mid
    else:
        l=mid

print(r)

"""

if a[-1]<=b[-1]:
    i=0
    while a:
        i+=1
        now=a.pop()
        if len(a)>0:
            while a[-1]==now:
                a.pop()
                i+=1
                if len(a)==0:
                    break
        ind=bisect_left(b,now)
        print(i,m-ind)
        if i>=m-(ind):
            print(now) 
            sys.exit()
    print(b[-1]+1)
else:
    print(b[-1]+1)
    """