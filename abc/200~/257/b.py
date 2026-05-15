
n,k,q=map(int,input().split())
a=list(map(int,input().split()))
l=list(map(int,input().split()))



ans=[]
for i in range(q):
    if a[l[i]-1]==n:
        continue
    else:
        if a[l[i]-1]+1 not in a:
            a[l[i]-1]+=1
print(*a)


