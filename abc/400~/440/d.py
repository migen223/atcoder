from bisect import bisect_left
n,q=map(int,input().split())
a=sorted(list(map(int,input().split())))


for j in range(q):
    x,y=map(int,input().split())
    ind0=bisect_left(a,x)
    l=ind0-1
    r=n
    #print("l,r=",l,r)
    while r-l>1:
        mid=(r+l)//2
        if a[mid]-x+1-(mid-ind0+1)>=y:
            r=mid
        else:
            l=mid
    #print("l=",l)
    print(x+y-1+r-ind0)
    #print("ans=",x+y-1+r-ind0)
