from sortedcontainers import SortedList
n,d=map(int,input().split())
a=list(map(int,input().split()))

sl=SortedList([-10**32,10**32])
def check(r,sl):
    #print(r,sl)
    if len(sl)==2:
        return True
    ind=sl.bisect_left(a[r])
    #print("sl",ind,sl,a[r])
    if abs(a[r]-sl[ind])>=d and abs(sl[ind-1]-a[r])>=d:
        return True
    return False

r=0
ans=0
for l in range(n):
    if r!=n:
        while check(r,sl):
            #print("True")
            sl.add(a[r])
            r+=1
            #print(l,r,sl)
            if r==n:
                break
    sl.discard(a[l])
    ans+=r-l

print(ans)