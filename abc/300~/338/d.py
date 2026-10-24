
n,m=map(int,input().split())
x=list(map(lambda x:int(x)-1,input().split()))
imos=[0]*(2*n)
l=[]
for i in range(m-1):
    l.append(min(abs(x[i]-x[i+1]),n-(abs(x[i]-x[i+1]))))
s=sum(l)

for i in range(m-1):
    ma=max(x[i],x[i+1])
    mi=min(x[i],x[i+1])
    if ma-mi>n//2:
        imos[ma]+=abs(l[i]-(n-l[i]))
        imos[ma+(mi+n-ma)]-=abs(l[i]-(n-l[i]))
    else:
        imos[mi]+=abs(l[i]-(n-l[i]))
        imos[ma]-=abs(l[i]-(n-l[i]))


for i in range(1,len(imos)):
    imos[i]+=imos[i-1]

ans=10**32
for i in range(n):
    ans=min(ans,s+imos[i]+imos[i+n])
print(ans)