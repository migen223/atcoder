
n=int(input())
p=998244353
keta=len(str(n))
bunsi=(n*(pow(10,n*keta,p)-1))%p
bunbo=10**keta-1
moddiv=pow(bunbo,-1,p)
print((bunsi*moddiv)%p)
