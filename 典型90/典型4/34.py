
n,k=map(int,input().split())
a=list(map(int,input().split()))

def check(m):
    dic={}
    for i in range(m):
        if a[i] in dic:
            dic[a[i]]+=1
        else:
            dic[a[i]]=1
    if len(dic)<=k:
        return True

    for i in range(n-m):
        dic[a[i]]-=1
        if dic[a[i]]==0:
            dic.pop(a[i])
        if a[i+m] in dic:
            dic[a[i+m]]+=1
        else:
            dic[a[i+m]]=1
        if len(dic)<=k:
            return True
        
    return False

l=0
r=n+1
while r-l>1:
    mid=(r+l)//2
    if check(mid):
        l=mid
    else:
        r=mid

print(l)
