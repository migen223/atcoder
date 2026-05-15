
n,m=map(int,input().split())

x=10**144
amax=0
while (amax)**2<=m:
    amax+=1

#print(amax)
for a in range(1,amax+1):
    if a>n:
        break
    if m%a==0:
        k=m//a
    else:
        k=m//a+1
    if k<=n:
        #print(m//a,a,a*(m//a+1))
        x=min(x,a*(k))
    
        #print(x)

if x==10**144:
    print(-1)
else:
    print(x)
