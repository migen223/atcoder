n,m=map(int,input().split())
a=list(map(int,input().split()))
def mysum(l,x):
    q=0
    for i in range(len(l)):
        q+=min(l[i],x)
    return q
if sum(a)<=m:
    print("infinite")
else:
    bottom=1
    top=max(a)+1
    while bottom!=(top+bottom)//2:
        mid=(top+bottom)//2
        s=mysum(a,mid)
        if s > m:
            top=mid
        elif s<=m:
            bottom=mid
        #print(top,bottom)

    print(bottom)


