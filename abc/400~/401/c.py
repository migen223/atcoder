from math import pow
n,k=map(int,input().split())

mod=int(pow(10,9))
if n<k:
    print(1)
else:     
    a=[1]*(n+1)
    a[k]=k
    count=0
    for i in range(n-k):
        
        a[k+i+1]=(2*a[k+i]-a[i])%mod
        #print(a[k+i+1])
        count+=1
    print(a[n]%(mod))
