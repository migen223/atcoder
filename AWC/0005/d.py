
n,k=map(int,input().split())
a=list(map(int,input().split()))

r=10**14+1
l=0

def check(l,ans,k):
    res=[]
    now=0
    for i in range(len(l)):
        now+=l[i]
        if now>=ans:
            res.append(now)
            now=0
    if len(res)>=k:
        return True
    return False

while r-l>1:
    mid=(r+l)//2
    if check(a,mid,k):
        l=mid
    else:
        r=mid

print(l)