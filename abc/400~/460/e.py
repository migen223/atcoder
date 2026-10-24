from math import lcm,gcd
t=int(input())
mod=998244353

for _ in range(t):
    n,m=map(int,input().split())
    keta=[]
    ns=str(n)
    for i in range(len(ns)+1):
        if n<10**(i+1):
            keta.append(n-10**i+1)
            break
        else:
            keta.append(10**(i+1)-10**(i))
   # print("keta",keta)
    ans=0
    for i in range(len(keta)):
        if (10**(i+1))%m==0 :
            ans+=(n//m)*(keta[i])
            ans%=mod
        else:
            x=m//gcd(10**(i+1)-1,m)
            #print("lcm",i+1,x)
            ans+=(n//x)*keta[i]
            ans%=mod
            
    print(ans)