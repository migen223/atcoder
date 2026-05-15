from sortedcontainers import SortedList
n=int(input())
a=list(map(int,input().split()))
def check(k):
    if k==0:
        return True
    lo=[]
    up=[]
    for i in range(k):
        lo.append(a[i])
        up.append(a[-1-i])
    up.sort()
    #print(lo)
    #print(up)
    for i in range(k):
        if lo[i]*2>up[i]:
            return False
    return True

l=0
r=n//2+1
while r-l>1:
    mid=(l+r)//2
    if check(mid):
        l=mid
    else:
        r=mid
    #print(l,r,mid)

print(l)

"""
ans=0
sl=SortedList(a)

while len(sl)>=2:
    if sl[0]*2>sl[len(sl)-1]:
        break
    now=sl.pop()
    ind=sl.bisect_right(now//2)-1
    sl.pop(ind)
    ans+=1
print(ans)
"""