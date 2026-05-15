
n,k=map(int,input().split())
a=list(map(int,input().split()))

l=0
r=max(a)+n*k+1

def check(m):
    res=0
    for i in range(n):
        if a[i]<m:
            d=m-a[i]
            if d%(i+1)==0:
                res+=d//(i+1)
            else:
                res+=d//(i+1)+1
            #print(d,(i+1))
        if res>k:
            #print("f",res,m)
            return False
    #print("t",res,m)
    return True


while r-l>1:
    m=(l+r)//2
    #print("lr",l,r)
    if check(m):
        l=m
    else:
        r=m

print(l)