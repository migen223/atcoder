
from random import randint
from itertools import combinations 
mod=998244353 
fact=[1,1,2]
for i in range(3,2*(10**5)+1):
    fact.append((fact[-1]*i)%mod)

rfact=[]
for i in range(2*(10**5)+1):
    rfact.append((pow(fact[i],-1,mod))%mod)

def C(n,k):
    return (fact[n]*rfact[n-k]*rfact[k])%mod
for  _ in range(10):
    n=randint(5,10)
    k=randint(1,n)
    a=[randint(1,10**9) for _ in range(n)]

    #print(n,k,a,"sample")
    #print()

    ans1=0
    #print()
    #print(a)
    for ci in combinations(a,k):
        #print(ci)
        res=sum(ci)
        ans1+=res*res
        ans1%=mod


    if k>1:
        ans=0
        nk=C(n,k)
        for i in range(n):
            ans+=(a[i]**2)*((nk*k)//n)
            ans%=mod

        r=[a[0]]
        for i in range(n-1):
            r.append((r[-1]+a[i+1])%mod)
        
        two=0
        for i in range(n-1):
            two+=a[i]*(r[-1]-r[i])
        ans+=two*2*C(n-2,k-2)
        #debug(ans,nk,C(n-2,k-2),two)
        #print(ans%mod)
    else:
        ans=0
        for i in range(n):
            ans+=a[i]*a[i]
        #print(ans%mod)
    ans%=mod
    #print(ans,ans1,"afij")
    if ans!=ans1:
        print(n,k)
        print(a)
        print(ans1,ans)
        print()