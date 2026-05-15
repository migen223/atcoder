
n,l,r=map(int,input().split())
a=list(map(int,input().split()))
ls=[0]*n
rs=[0]*n
ls[0]=l-a[0]
rs[-1]=r-a[-1]
for i in range(1,n):
    ls[i]=ls[i-1]+(l-a[i])
    rs[-1-i]=rs[-i]+(r-a[-i-1])
#print(ls)
#print(rs)
s=sum(a)

lmin=[0]*n
rmin=[0]*n
lmi=10**32
rmi=10**32
for i in range(n):
    lmi=min(ls[i],lmi)
    rmi=min(rs[-1-i],rmi)
    lmin[i]=lmi
    rmin[-1-i]=rmi

minus=0
for i in range(n-1):
    minus=min(minus,lmin[i]+rmin[i+1])
minus=min(minus,rmin[0])
minus=min(minus,lmin[-1])
#print(lmin)
#print(rmin)
print(s+minus)